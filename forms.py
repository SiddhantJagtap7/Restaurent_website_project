from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    # Add fields for the customer's details
    name = forms.CharField(
        max_length=120, 
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your Full Name',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'your@email.com',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        })
    )
    phone = forms.CharField(
        max_length=30, 
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Phone Number (Optional)',
            'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
        })
    )

    class Meta:
        model = Reservation
        # We only need these fields from the model itself
        fields = ['date', 'time', 'guests']
        
        # Add widgets to control how the fields are rendered
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date', # This makes it choosable and typeable
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
                }
            ),
            'time': forms.TimeInput(
                attrs={
                    'type': 'time', # This adds a time picker
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
                }
            ),
            'guests': forms.NumberInput(
                attrs={
                    'min': '1', # Guests can't be less than 1
                    'class': 'w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500'
                }
            )
        }