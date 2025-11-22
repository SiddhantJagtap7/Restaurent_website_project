import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_project.settings')
django.setup()

from restaurant.models import Reservation, Customer
from datetime import date, time as datetime_time

print("=" * 60)
print("TESTING CAPACITY SYSTEM")
print("=" * 60)

# Test date and time
test_date = date(2025, 11, 25)
test_time = datetime_time(19, 0)  # 7:00 PM

print(f"\nTest Slot: {test_date} at {test_time}")
print("-" * 60)

# Create test customers and reservations
customers_data = [
    ("Test Customer 1", "test1@example.com", "+919876543210", 10),
    ("Test Customer 2", "test2@example.com", "+919876543211", 15),
    ("Test Customer 3", "test3@example.com", "+919876543212", 8),
]

print("\nCreating test reservations...")
for name, email, phone, guests in customers_data:
    customer, created = Customer.objects.get_or_create(
        email=email,
        defaults={'name': name, 'phone': phone}
    )
    
    reservation = Reservation.objects.create(
        customer=customer,
        date=test_date,
        time=test_time,
        guests=guests
    )
    print(f"[OK] Created: {name} - {guests} guests")

# Check total capacity
from django.db.models import Sum
total_guests = Reservation.objects.filter(
    date=test_date,
    time=test_time
).aggregate(total=Sum('guests'))['total'] or 0

remaining = 45 - total_guests

print("\n" + "=" * 60)
print("CAPACITY SUMMARY")
print("=" * 60)
print(f"Total Guests Booked: {total_guests}")
print(f"Remaining Capacity: {remaining} seats")
print(f"Number of Reservations: {Reservation.objects.filter(date=test_date, time=test_time).count()}")

print("\n" + "=" * 60)
print("[SUCCESS] TEST COMPLETE!")
print("=" * 60)
print(f"\nNow try booking for {test_date} at 7:00 PM on the website.")
print(f"You should see: 'Tables available! {remaining} seats remaining'")
print("=" * 60)
