from .models import Comment, Products, Category
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text' , 'star']



class AddProductForm(forms.ModelForm):
    class  Meta:
        model = Products
        fields = ['title', 'content', 'cover', 'star', 'price', 'active', 'discouont', 'inventory', 'category']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'star' : forms.Select(attrs={'class':'form-select custom-select'}),
            'category' : forms.Select(attrs={'class':'form-select custom-select'}),

            # 'active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'cover':forms.FileInput(attrs={'class':'btn-chang-avatar'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'discouont': forms.TextInput(attrs={'class':'form-control'}),
            'price': forms.TextInput(attrs={'class':'form-control'}),
            'content':SummernoteWidget(),

            # 'content': forms.TextInput(attrs={'class':'form-control'}),
            
        }


class AddCategory(forms.ModelForm):
    class  Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),             
        }

        
