from .models import Tickets, TicketMessage
from django import forms




class TicketForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = [ 'title', 'priority',]
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            # 'email' : forms.EmailInput(attrs={'class':'form-control'}),

            'priority':forms.Select(attrs={'class':'form-control'}),
            # 'status':forms.TextInput(attrs={'class':'form-control'}),
            # 'active':forms.TextInput(attrs={'class':'form-control'}),
            # 'subject':forms.TextInput(attrs={'class':'form-control'}),
            # 'image':forms.ImageField(),
            # 'image' : forms.FileInput(attrs={'class':'btn-chang-avatar'})

            
        }



class TicketMessageForm(forms.ModelForm):
    class Meta:
        model = TicketMessage
        fields = [ 'file', 'message', ]
        widgets = {
            'file' : forms.FileInput(attrs={'class':'btn-chang-avatar'})

            
        }