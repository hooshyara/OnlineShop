from .models import Products

# def comment(request):
    
#     my_comment = Comment.objects.filter(user=request.user)
#     return {'comment':my_comment}


def discount(request):
    product = Products.objects.filter(active=True)
    for i in product:
        print(i.discouont)
        end_price = i.price - (i.price * (i.discouont/100))
        i.second_price = end_price
        print(int(end_price))
        return {'end_price':int(end_price)}