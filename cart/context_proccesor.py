from .models import Cart



def cart(request):
    try:
        my_cart = Cart.objects.filter(user=request.user)
        total_price = 0
        for i in my_cart:
            product_total_price =  int(i.products.price - (i.products.price * (i.products.discouont/100)))
            total_price = total_price + product_total_price * i.count
        return {'my_cart':my_cart, 'total':total_price}
    except:
        return {}




