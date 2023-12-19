from django import forms
from .models import Contact


class ContantForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name' , 'email', 'phone_number', 'subject', 'text', ]
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone_number':forms.TextInput(attrs={'class':'form-control'}),
            'subject':forms.TextInput(attrs={'class':'form-control'}),
            

            
            
        }