from django.shortcuts import render, redirect
from django.contrib import messages
from rest_framework import viewsets
from .models import MenuItem, Reservation, Customer
from .serializers import MenuItemSerializer, ReservationSerializer
from .forms import ReservationForm
from django.db import IntegrityError
from .notifications import send_all_notifications
import logging

logger = logging.getLogger(__name__)

# --- Website Views ---

def index(request):
    """
    Renders the homepage.
    """
    return render(request, 'index.html')


# --- NEW FUNCTION ---
def menu_view(request):
    """
    Renders the menu page.
    """
    # Get all available menu items
    items = MenuItem.objects.filter(available=True)
    
    # Get the unique categories from the items
    category_names = items.values_list('category', flat=True).distinct()
    
    # We will build a list of categories, each containing its items
    categories = []
    
    for category_name in MenuItem.CATEGORY_CHOICES:
        # category_name is a tuple like ('starter', 'Starter')
        # We check items that match the internal name (e.g., 'starter')
        category_items = items.filter(category=category_name[0])
        
        # Only add the category to our list if it has items
        if category_items.exists():
            categories.append({
                'name': category_name[1], # The display name (e.g., 'Starter')
                'items': category_items
            })

    context = {
        'categories': categories
    }
    return render(request, 'menu.html', context)
# --- END NEW FUNCTION ---


def reservation_view(request):
    """
    Handles the reservation form.
    """
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            # Get the customer details from the form
            customer_name = form.cleaned_data['name']
            customer_email = form.cleaned_data['email']
            customer_phone = form.cleaned_data['phone']
            
            # Find or create the customer
            customer, created = Customer.objects.get_or_create(
                email=customer_email,
                defaults={
                    'name': customer_name,
                    'phone': customer_phone
                }
            )
            
            # If customer already exists, just update their name/phone
            if not created:
                customer.name = customer_name
                customer.phone = customer_phone
                customer.save()

            try:
                # Maximum capacity check
                MAX_CAPACITY = 45
                requested_guests = form.cleaned_data['guests']
                
                # Check if requested guests exceeds maximum
                if requested_guests > MAX_CAPACITY:
                    messages.error(request, f'Maximum {MAX_CAPACITY} guests allowed per reservation.')
                    return render(request, 'reservation.html', {'form': form})
                
                # Calculate current capacity for this time slot
                from django.db.models import Sum
                existing_reservations = Reservation.objects.filter(
                    date=form.cleaned_data['date'],
                    time=form.cleaned_data['time']
                )
                total_booked_guests = existing_reservations.aggregate(
                    total=Sum('guests')
                )['total'] or 0
                
                remaining_capacity = MAX_CAPACITY - total_booked_guests
                
                # Check if there's enough capacity
                if requested_guests > remaining_capacity:
                    if remaining_capacity > 0:
                        messages.error(request, f'Only {remaining_capacity} seats remaining for this time slot. Please choose another time or reduce the number of guests.')
                    else:
                        messages.error(request, 'This time slot is fully booked. Please choose another time.')
                    return render(request, 'reservation.html', {'form': form})
                
                # Create the reservation but don't save to DB yet
                reservation = form.save(commit=False)
                # Attach the customer to it
                reservation.customer = customer
                # Now save the reservation
                reservation.save()
                
                # Send email notifications to staff and customer
                try:
                    notification_results = send_all_notifications(reservation, customer)
                    if notification_results['staff_email']:
                        logger.info("Staff notification email sent successfully")
                    if notification_results['customer_email']:
                        logger.info("Customer confirmation email sent successfully")
                except Exception as e:
                    # Log the error but don't break the reservation process
                    logger.error(f"Failed to send notifications: {str(e)}")
                
                # Add a success message
                messages.success(request, 'Your reservation has been submitted! We will contact you to confirm.')
                
                # Redirect to the homepage
                return redirect('index')

            except Exception as e:
                # Catch any other errors
                logger.error(f"Reservation error: {str(e)}")
                messages.error(request, 'An error occurred. Please try again.')
                # We fall through and re-render the form
        
        else:
            # Form is invalid, add an error message
            messages.error(request, 'There was an error. Please check the form and try again.')

    else:
        form = ReservationForm()

    context = {'form': form}
    return render(request, 'reservation.html', context)


def check_availability(request):
    """
    API endpoint to check if tables are available for a given date, time, and number of guests.
    Returns JSON response with availability status.
    Maximum capacity: 45 guests per time slot.
    """
    from django.http import JsonResponse
    from django.db.models import Sum
    
    # Maximum restaurant capacity per time slot
    MAX_CAPACITY = 45
    
    if request.method == 'GET':
        date = request.GET.get('date')
        time = request.GET.get('time')
        guests_str = request.GET.get('guests', '1')
        
        if not date or not time:
            return JsonResponse({
                'available': None,
                'message': 'Please select both date and time'
            })
        
        try:
            requested_guests = int(guests_str)
        except (ValueError, TypeError):
            requested_guests = 1
        
        # Validate guest count
        if requested_guests > MAX_CAPACITY:
            return JsonResponse({
                'available': False,
                'message': f'❌ Maximum {MAX_CAPACITY} guests allowed per reservation.'
            })
        
        # Calculate total guests already booked for this date/time
        existing_reservations = Reservation.objects.filter(
            date=date,
            time=time
        )
        
        total_booked_guests = existing_reservations.aggregate(
            total=Sum('guests')
        )['total'] or 0
        
        # Calculate remaining capacity
        remaining_capacity = MAX_CAPACITY - total_booked_guests
        
        if requested_guests > remaining_capacity:
            if remaining_capacity > 0:
                return JsonResponse({
                    'available': False,
                    'message': f'❌ Only {remaining_capacity} seats remaining for this time slot. Please choose another time or reduce guests.'
                })
            else:
                return JsonResponse({
                    'available': False,
                    'message': '❌ This time slot is fully booked. Please choose another time.'
                })
        else:
            return JsonResponse({
                'available': True,
                'message': f'✅ Tables available! {remaining_capacity} seats remaining for this time slot.',
                'remaining_capacity': remaining_capacity
            })
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)


# --- API Views ---
# (You already have these)

class MenuItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows menu items to be viewed or edited.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows reservations to be viewed or edited.
    """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer