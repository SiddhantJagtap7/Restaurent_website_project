import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from restaurant.models import Reservation
from django.db.models import Sum

print("=" * 50)
print("RESERVATION DATABASE CHECK")
print("=" * 50)

total = Reservation.objects.count()
print(f"\nTotal Reservations: {total}\n")

if total > 0:
    print("Recent Reservations:")
    print("-" * 50)
    for r in Reservation.objects.all().order_by('-created_at')[:10]:
        print(f"ID: {r.id} | Date: {r.date} | Time: {r.time} | Guests: {r.guests} | Customer: {r.customer.name}")
    
    # Check for duplicate time slots
    print("\n" + "=" * 50)
    print("CAPACITY CHECK PER TIME SLOT")
    print("=" * 50)
    
    from django.db.models import Count
    time_slots = Reservation.objects.values('date', 'time').annotate(
        total_guests=Sum('guests'),
        num_reservations=Count('id')
    ).order_by('-date', 'time')
    
    for slot in time_slots[:5]:
        print(f"Date: {slot['date']} | Time: {slot['time']} | Total Guests: {slot['total_guests']} | Reservations: {slot['num_reservations']}")
else:
    print("No reservations found in database!")

print("\n" + "=" * 50)
