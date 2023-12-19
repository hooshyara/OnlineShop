from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'city', 'address', 'description', 'post_id']
        widgets = {
            'user' : forms.TextInput(attrs={'class':'form-control'}),
            'date' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'post_id' : forms.TextInput(attrs={'class':'form-control'}),

        }

class CartForm(forms.Form):
    product_count = forms.IntegerField()