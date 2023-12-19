from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import *

def contact_us_view(request):
    form = ContantForm()
 
    if request.method == 'POST':
        form = ContantForm(request.POST)
        if form.is_valid():
            print('ddddddddd')
            form.save()
            return redirect(reverse('contact:contact'))
        else:
            print(form.errors)
    return render(request, 'contact.html', context={'form':form})