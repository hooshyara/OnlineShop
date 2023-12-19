from django.shortcuts import render, redirect, get_object_or_404
from products.models import Products
from .models import Cart, Order, OrderItem
from .forms import CartForm, OrderForm


def add_to_cart(request, product_id):
    form = CartForm(request.POST)
    
    product = Products.objects.get(id=product_id)
    if Cart.objects.filter(user=request.user, products=product).exists():
        cart = Cart.objects.get(user=request.user, products=product)
        if form.is_valid():
            cart.count = cart.count + int(form.data['product_count'])
            cart.save()
            cart.end_price = str(cart.count * product.second_price)
        else:
            cart.count += 1
            cart.end_price = str(int(cart.end_price) + product.second_price)
        
        cart.save()
    else:
        try:
            count = form.data['product_count']
        except:
            count = 1
        cart = Cart.objects.create(
            user=request.user, 
            products=product,
            count = count,
            end_price = str(product.second_price * int(count)), 
        )
        cart.save()
    return redirect('cart:cart_detail' )

def cart_detail(request):
    cart = Cart.objects.filter(user=request.user)
    total_price = 0
    for i in cart:
        total_price = total_price + i.products.second_price * i.count

    return render(request,  'cart.html', context={'cart':cart, "total_price":total_price})

def remove_from_cart(request, product_id):
    product = Products.objects.get(id=product_id)
    cart = get_object_or_404(Cart, products=product, user=request.user)
    cart.delete()
    return redirect('cart:cart_detail')

def chetout(request):
    cart = Cart.objects.filter(user=request.user)
    form = OrderForm()

    
    if request.method == "POST":
        form = OrderForm(request.POST)

        total_price = 0
        for i in cart:
            total_price = total_price + i.products.second_price * i.count
        order = Order.objects.create(
            user = request.user,
            first_name = form.data['first_name'],
            last_name = form.data['last_name'],
            city = form.data['city'],
            # description = form.data['description'],
            post_id = form.data['post_id'],
            totla_price = total_price
        )
        order.save()
        for item in cart:
            product = Products.objects.get(id=item.products.id)
            orderItem = OrderItem.objects.create(
                user = request.user,
                order = order,
                product = product,
                product_price = item.products.price,
                product_count = item.count,
                product_cost = item.end_price

            )
            orderItem.save()
            product.inventory -= item.count
            product.save()
            product_cart = Cart.objects.get(user=request.user, products=product)
            product_cart.delete()
            return render(request, 'compelete_order.html')
    return render(request, 'chekout.html', context={'cart':cart, 'formOrder':form})



