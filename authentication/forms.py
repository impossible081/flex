# My Django imports
from django import forms

# My App imports
from authentication.models import Customer

class CustomerRegistrationForm(forms.ModelForm):
    fullname = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Full name',
                                   }
                               ))
    email = forms.EmailField(required=True, max_length=255, help_text='A valid email address is Required!',
                             widget=forms.TextInput(
                                 attrs={
                                     'class':'form-control',
                                     'placeholder':'Email Address',
                                     'type':'email'
                                 }
                             ))
    phoneNumber = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Phone number',
                                       'type':'number'
                                   }
                               ))
    password = forms.CharField(required=True, help_text='Password must contain at least 6 characters',
                               widget=forms.TextInput(
                                   attrs={
                                       'class':'form-control',
                                       'placeholder':'Password',
                                       'type':'Password',
                                   }
                               ))
    
    class Meta:
        model = Customer
        fields = ('fullname', 'email', 'phoneNumber', 'password')
        
        def clean_password(self):
            password = self.cleaned_data.get('password')
            
            if len(password) < 6:
                raise forms.ValidationError('Password too short')
            
            return password