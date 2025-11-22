from django.db import models
from django.db.models import JSONField # Import the standard, built-in JSONField

class MenuItem(models.Model):
    # Comprehensive categories based on the menu card
    CATEGORY_CHOICES = [
        # Starters
        ('chinese_veg_starter', 'Chinese Veg Starter'),
        ('chinese_nonveg_starter', 'Chinese Non-Veg Starter'),
        ('veg_indian_snacks', 'Veg Indian Snacks'),
        ('nonveg_indian_snacks', 'Non-Veg Indian Snacks'),
        
        # Soups
        ('soups', 'Soups'),
        
        # Snacks
        ('snacks', 'Snacks'),
        
        # Mocktails
        ('mocktail', 'Mocktail'),
        
        # Tandoori
        ('chinese_veg_tandoori', 'Chinese Veg Tandoori Starter'),
        ('chinese_nonveg_tandoori', 'Chinese Non-Veg Tandoori Starter'),
        
        # Seafood
        ('bombil_seafood', 'Bombil Sea Food'),
        
        # Quick Bites
        ('quick_bites', 'Quick Bites'),
        
        # Rice & Noodles
        ('chinese_veg_rice', 'Chinese Veg Rice'),
        ('chinese_veg_noodles', 'Chinese Veg Noodles'),
        ('chinese_nonveg_rice', 'Chinese Non-Veg Rice'),
        ('chinese_nonveg_noodles', 'Chinese Non-Veg Noodles'),
        
        # Main Course
        ('veg_indian_main', 'Veg - Indian Main Course'),
        ('vegetable', 'Vegetable'),
        ('dum', 'Dum'),
        ('paneer', 'Paneer'),
        
        # Others
        ('fish_tandoori', 'Fish Tandoori'),
        ('ginger', 'Ginger'),
        ('breads', 'Breads'),
    ]
    
    # Subcategory choices for better organization
    SUB_CATEGORY_CHOICES = [
        # Starters subcategories
        ('momos', 'Momos'),
        ('chilly', 'Chilly'),
        ('manchurian', 'Manchurian'),
        ('dry', 'Dry'),
        ('gravy', 'Gravy'),
        ('rolls', 'Rolls'),
        
        # Soup types
        ('chinese_soup', 'Chinese Soup'),
        ('hot_sour_soup', 'Hot and Sour Soup'),
        ('clear_soup', 'Clear Soup'),
        
        # Snacks
        ('steam', 'Steam'),
        ('fry', 'Fry'),
        
        # Tandoori
        ('paneer_tikka', 'Paneer Tikka'),
        ('chicken_tikka', 'Chicken Tikka'),
        ('tandoori', 'Tandoori'),
        
        # Rice types
        ('fried_rice', 'Fried Rice'),
        ('schezwan_rice', 'Schezwan Rice'),
        ('triple_schezwan', 'Triple Schezwan'),
        ('manchurian_rice', 'Manchurian Rice'),
        ('burnt_garlic', 'Burnt Garlic'),
        
        # Noodles types
        ('hakka_noodles', 'Hakka Noodles'),
        ('schezwan_noodles', 'Schezwan Noodles'),
        ('triple_schezwan_noodles', 'Triple Schezwan Noodles'),
        ('manchurian_noodles', 'Manchurian Noodles'),
        ('cheese_noodles', 'Cheese Noodles'),
        
        # Main course
        ('dal', 'Dal'),
        ('masala', 'Masala'),
        ('curry', 'Curry'),
        ('paneer_dishes', 'Paneer Dishes'),
        
        # Others
        ('egg', 'Egg'),
        ('chicken', 'Chicken'),
        ('mutton', 'Mutton'),
        ('prawns', 'Prawns'),
    ]
    
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    
    # Use JSONField to store multiple prices/sizes (e.g., [{"size": "Half", "price": 180}])
    sizes_and_prices = JSONField(default=list, blank=True)
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    # Optional sub-category for better filtering
    sub_category = models.CharField(max_length=50, choices=SUB_CATEGORY_CHOICES, blank=True, null=True) 
    
    available = models.BooleanField(default=True)
    
    def __str__(self):
        # Display the lowest price for the admin list
        if self.sizes_and_prices:
            try:
                min_price = min(item['price'] for item in self.sizes_and_prices if item.get('price') is not None)
                return f"{self.name} — from ₹{min_price}"
            except ValueError:
                pass
        return self.name

class Customer(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(unique=True) 
    phone = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1) 
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    
    # No unique_together constraint - multiple reservations allowed per time slot
    # Total capacity is checked in the view logic

    def __str__(self):
        return f"Reservation {self.id} for {self.customer} on {self.date} {self.time} ({self.guests} guests)"