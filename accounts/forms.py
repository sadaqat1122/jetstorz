from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            # Get the existing classes attribute or an empty string if it doesn't exist
            classes = self.fields[field].widget.attrs.get('class', '')
            # Append the 'form-control' class to the existing classes (separated by space)
            classes += ' form-control'
            # Update the widget's attributes with the modified 'class' attribute
            self.fields[field].widget.attrs['class'] = classes

            # Set the placeholder attribute based on the field name (capitalized and with spaces)
            placeholder_text = field.replace("_", " ").capitalize()
            self.fields[field].widget.attrs['placeholder'] = f'Enter {placeholder_text}'

    def clean(self):
    	cleaned_data = super(RegistrationForm, self).clean()
    	password = cleaned_data.get('password')
    	confirm_password = cleaned_data.get('confirm_password')


    	if password != confirm_password:
    		raise forms.ValidationError(
    			"Password does not match.")
