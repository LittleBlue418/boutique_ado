from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        # Dictionary of placeholder text
        placeholders = {
            'default_phone_number': 'Phone number',
            'default_postcode': 'Post Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County or State',
        }

        # Autofocus on the full name field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # staring required fields
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]

                # setting the placeholder text using our dictionary
                self.fields[field].widget.attrs['placeholder'] = placeholder
            # adding a css class
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input'
            # removing the form fields label
            self.fields[field].label = False
