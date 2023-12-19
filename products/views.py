from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from .models import Products, Comment, Category
from django.views import generic
from .forms import CommentForm, AddProductForm, AddCategory
from cart.forms import CartForm
from django.core.paginator import Paginator
from .filters import ProductFilter


def product_list(request, category=None):
    if category:
        categoryobj = Category.objects.get(name=category)
        product = get_list_or_404(Products, category=categoryobj)
        paginator = Paginator(product, 2)
        page = request.GET.get('page', 1)
        page_obj = paginator.get_page('page')

    else:
        category = Category.objects.all()
        product = Products.objects.filter(active=True)
        filter = ProductFilter(request.GET, queryset=product)
        paginator = Paginator(filter.qs, 2)
        page = request.GET.get('page', 1)
        page_obj = paginator.get_page(page)
        print(paginator.page(1))

    categorys = []
    for item in Category.objects.all():
        category_name = {}
        length = len(Products.objects.filter(category__name=item.name))
        category_name["name"] = item.name
        category_name["length"] = length
        categorys.append(category_name)

    return render(request, 'product_list.html', context={"page_obj": page_obj, 'category': categorys})


def product_detail(request, pk):
    cart_form = CartForm()
    product = Products.objects.get(id=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)

        comment = Comment.objects.create(
            product=product,
            user=request.user,
            text=form.data['text'],
            star=form.data['star']

        )
        comment.save()
        return redirect(reverse('products:product_list'))

    return render(request, 'product_detail.html',
                  context={'product': product, 'form': form, 'cart_form': cart_form, })


def search_product(request):
    if request.method == "POST":
        title = request.POST['search']
        product = Products.objects.filter(title__contains=title)
        if product.exists():

            return render(request, 'product_list.html', context={'page_obj': product})
        else:
            return render(request, 'search_not_found.html')


def add_product(request):
    if request.user.is_superuser:

        if request.method == "POST":
            form = AddProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile_view')
            else:
                print(form.errors)
        return redirect('blog:blog_list')


def add_category(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = AddCategory(request.POST)
            if form.is_valid():
                form.save()
                return redirect('accounts:profile_view')
            else:
                print(form.errors)
        return redirect('blog:blog_list')


def delete_product(request, pk):
    if request.user.is_superuser:
        product = Products.objects.get(id=pk)
        product.delete()
        return redirect(reverse('accounts:profile_view'))
    return redirect('blog:blog_list')


def update_product(request, pk):
    if request.user.is_superuser:
        product = get_object_or_404(Products, id=pk)
        form = AddProductForm(instance=product)
        if request.method == "POST":
            print('aaa')

            form = AddProductForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                print('qqqqq')
                form.save()
                return redirect(reverse('accounts:profile_view'))
            else:
                print(form.errors)
        return render(request, 'product_update.html', context={'UPform': form, 'product': product})


def category_list(request):
    category = Category.objects.all()
    return render(request, 'category.html', context={'categorys': category})
