"""
Email notification functions for restaurant reservations.
Sends notifications to staff and customers when reservations are made.
"""

from django.core.mail import send_mail
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


def send_reservation_email_to_staff(reservation, customer):
    """
    Send email notification to restaurant staff about a new reservation.
    
    Args:
        reservation: Reservation object
        customer: Customer object
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        subject = f'New Reservation - Mata Pita Da Dhaba'
        
        message = f"""
New Reservation Received!

Customer Details:
-----------------
Name: {customer.name}
Email: {customer.email}
Phone: {customer.phone}

Reservation Details:
-------------------
Date: {reservation.date.strftime('%B %d, %Y')}
Time: {reservation.time.strftime('%I:%M %p')}
Number of Guests: {reservation.guests}

Please contact the customer to confirm the reservation.

---
Mata Pita Da Dhaba
Sai Wadi, Madh, Marve Road, Malad West, Mumbai
Phone: +91-9373066280
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.MANAGER_EMAIL],
            fail_silently=False,
        )
        
        logger.info(f"Staff notification email sent for reservation {reservation.id}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send staff email: {str(e)}")
        return False


def send_reservation_email_to_customer(reservation, customer):
    """
    Send confirmation email to customer about their reservation.
    
    Args:
        reservation: Reservation object
        customer: Customer object
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        subject = f'Reservation Confirmation - Mata Pita Da Dhaba'
        
        message = f"""
Dear {customer.name},

Thank you for choosing Mata Pita Da Dhaba!

Your reservation has been received and is pending confirmation.

Reservation Details:
-------------------
Date: {reservation.date.strftime('%B %d, %Y')}
Time: {reservation.time.strftime('%I:%M %p')}
Number of Guests: {reservation.guests}

We will contact you shortly at {customer.phone} to confirm your reservation.

If you need to make any changes, please contact us:
Phone: +91-9373066280
Email: siddhantjagtap0707@gmail.com

Location:
Sai Wadi, Madh, Marve Road, Malad West, Mumbai

We look forward to serving you!

Best regards,
Mata Pita Da Dhaba Team
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[customer.email],
            fail_silently=False,
        )
        
        logger.info(f"Customer confirmation email sent to {customer.email}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send customer email: {str(e)}")
        return False


def send_all_notifications(reservation, customer):
    """
    Send all notifications (email to staff and customer).
    
    Args:
        reservation: Reservation object
        customer: Customer object
    
    Returns:
        dict: Status of each notification type
    """
    results = {
        'staff_email': False,
        'customer_email': False,
    }
    
    # Send email to staff
    results['staff_email'] = send_reservation_email_to_staff(reservation, customer)
    
    # Send email to customer
    results['customer_email'] = send_reservation_email_to_customer(reservation, customer)
    
    # Log summary
    successful = sum(results.values())
    logger.info(f"Notifications sent: {successful}/2 successful")
    
    return results
