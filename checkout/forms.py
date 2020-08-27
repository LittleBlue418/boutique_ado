from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                    'street_address1', 'street_address2',
                    'town_or_city', 'postcode', 'country',
                    'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # Dictionary of placeholder text
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone number',
            'postcode': 'Post Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County or State',
        }

        # Autofocus on the full name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # staring required fields
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # setting the placeholder text using our dictionary
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # adding a css class
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # removing the form fields label
            self.fields[field].label = False
