from .models import Favorite
from django.shortcuts import render 


def favorite(request):
    try:
        wish_list = Favorite.objects.filter(user=request.user)
        return {'wish_list':wish_list}
    except:
        return {}