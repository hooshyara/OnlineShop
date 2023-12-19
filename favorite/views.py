from django.shortcuts import render ,redirect, get_object_or_404, reverse
from .models import Favorite
from products.models import Products



def add_to_favorite(request, product_id):

    
    product = Products.objects.get(id=product_id)
    if Favorite.objects.filter(user=request.user, product=product).exists():
        pass
    else:
        favorite = Favorite.objects.create(
            user = request.user,
            product=product,
        )
        favorite.save()
    return redirect('products:product_list')



def favorite_items(request):
    favorite = Favorite.objects.filter(user=request.user)

    return render(request, 'wish_list.html', context={'favorite':favorite})



def remove_from_wishlist(request, product_id=None):
    if product_id:
        product = Products.objects.get(id=product_id)
        print(request.user)

        favorite = Favorite.objects.get(product=product ,user=request.user)
        favorite.delete()

        return redirect(reverse('favorite:wishlist'))
    else:
        favorite = Favorite.objects.filter(user=request.user)
        for item in favorite:
            favorite_obj = Favorite.objects.get(id=item.id)
            favorite_obj.delete()

        return redirect(reverse('accounts:profile_view')) 
        


