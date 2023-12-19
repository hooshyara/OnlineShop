from django import forms
from .models import User
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mobile','first_name','last_name', 'password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mobile', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['mobile', 'first_name', 'last_name', 'born_dateTime', 'gender', 'province', 'city', 'address', 'national_id', 
                  'post_id', 'profile_picture', ]
        widgets = {
            'mobile' : forms.TextInput(attrs={'class':'form-control'}),
            'born_dateTime' : forms.TextInput(attrs={'class':'form-control'}),
            'first_name' : forms.TextInput(attrs={'class':'form-control'}),
            'last_name' : forms.TextInput(attrs={'class':'form-control'}),
            'gender' : forms.Select(attrs={'class':'form-select custom-select'}),
            'province' : forms.TextInput(attrs={'class':'form-control'}),
            'city' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
            'national_id' : forms.TextInput(attrs={'class':'form-control'}),
            'post_id' : forms.TextInput(attrs={'class': 'form-control'}),
            'profile_picture' : forms.FileInput(attrs={'class':'btn-chang-avatar'})
        }
        
    
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['born_dateTime'] = JalaliDateField(label=('date'), 
            widget=AdminJalaliDateWidget 
        )

        
        


class ChangePassword(forms.Form):
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    

    
        