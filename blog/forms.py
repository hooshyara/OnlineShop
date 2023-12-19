from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text' , 'star']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']


class AddBlogForm(forms.ModelForm):
    class  Meta:
        model = Blogs
        fields = ['title', 'content', 'cover',  'is_active',]
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'cover':forms.FileInput(attrs={'class':'btn-chang-avatar'}),
            # 'is_active': forms.CheckboxInput(attrs={'class':'form-control'}),
            'content': SummernoteWidget(), 
        }