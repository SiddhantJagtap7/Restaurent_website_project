from django.contrib import admin
from .models import MenuItem, Customer, Reservation

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for Menu Items
    """
    # Display key fields in the list view
    list_display = ('name', 'category', 'sub_category', 'display_price', 'available')
    
    # Add filters for easy navigation
    list_filter = ('category', 'sub_category', 'available')
    
    # Enable search functionality
    search_fields = ('name', 'description')
    
    # Make availability editable from list view
    list_editable = ('available',)
    
    # Organize fields in the edit form
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'available')
        }),
        ('Categorization', {
            'fields': ('category', 'sub_category')
        }),
        ('Pricing', {
            'fields': ('sizes_and_prices',),
            'description': 'Add prices in JSON format: [{"size": "Full", "price": 200}, {"size": "Half", "price": 120}]'
        }),
    )
    
    # Set default ordering
    ordering = ('category', 'sub_category', 'name')
    
    # Custom method to calculate and display the price range from the JSONField
    def display_price(self, obj):
        if obj.sizes_and_prices:
            try:
                prices = [item.get('price', 0) for item in obj.sizes_and_prices if isinstance(item.get('price'), (int, float))]
                if prices:
                    min_price = min(prices)
                    max_price = max(prices)
                    if min_price == max_price:
                        return f"₹{min_price}"
                    return f"₹{min_price} - ₹{max_price}"
            except (ValueError, TypeError):
                return "—"
        return "N/A"
    
    display_price.short_description = 'Price Range'
    
    # Add custom admin actions
    actions = ['mark_available', 'mark_unavailable']
    
    def mark_available(self, request, queryset):
        updated = queryset.update(available=True)
        self.message_user(request, f'{updated} items marked as available.')
    mark_available.short_description = 'Mark selected items as available'
    
    def mark_unavailable(self, request, queryset):
        updated = queryset.update(available=False)
        self.message_user(request, f'{updated} items marked as unavailable.')
    mark_unavailable.short_description = 'Mark selected items as unavailable'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """
    Admin configuration for Customers
    """
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email', 'phone')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """
    Admin configuration for Reservations
    """
    list_display = ('id', 'customer', 'date', 'time', 'guests', 'confirmed', 'created_at')
    list_filter = ('date', 'time', 'confirmed')
    search_fields = ('customer__name', 'customer__email')
    list_editable = ('confirmed',) # Allows you to confirm reservations from the list view