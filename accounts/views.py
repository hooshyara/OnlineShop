from django.shortcuts import render, redirect, reverse, get_object_or_404, get_list_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm, SignupForm, ProfileForm, ChangePassword
from .models import User
from products.models import Comment, Products
from favorite.models import Favorite
from cart.models import *
from products.forms import AddProductForm, AddCategory
from blog.models import Blogs
from blog.forms import AddBlogForm
from tickets.models import Tickets, TicketMessage
from contact.models import Contact


def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        mobile = form.data['mobile']
        password = form.data['password']
        user = authenticate(mobile=mobile, password=password)
        if check_password(password, user.password):
            user.is_active = True
            user.save()
            auth_login(request, user)
        return redirect(reverse('products:product_list'))


def logout(request):
    auth_logout(request)
    return redirect(reverse('Home:HomeView'))


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid:
            user = User.objects.create(
                mobile=form.data['mobile'],
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                password=make_password(form.data['password']),
            )
            user.save()
            user = authenticate(mobile=form.data['mobile'], password=form.data['password'])

            return redirect(reverse('products:product_list'))
    return render(request, 'registration/signup.html', context={'form': form})


def profile_view(request):
    user_list = User.objects.all()
    favorite = Favorite.objects.filter(user=request.user)
    my_comment = Comment.objects.filter(user=request.user)
    form = ProfileForm(instance=request.user)
    add_product = AddProductForm()
    add_blog = AddBlogForm()
    add_category = AddCategory()
    password_form = ChangePassword()
    cart = Cart.objects.filter(user=request.user)
    if request.user.is_superuser:
        orderItem = Order.objects.all()
        order = Order.objects.all()
        blog = Blogs.objects.all()
        product = Products.objects.all()
        ticket = Tickets.objects.all().order_by('-priority')
        contact = Contact.objects.all()
        if request.method == 'POST':
            print('ddd')
            code = request.POST['search']
            ticket = Tickets.objects.filter(code__contains=code)
            if ticket.exists():
                return render(request, 'profile.html',
                              context={'favorite': favorite, 'form': form, 'pass_form': password_form, 'cart': cart,
                                       'comment': my_comment, 'products': product, 'add_form': add_product,
                                       'user': user_list, 'blog': blog, 'add_blog': add_blog, 'ticket': ticket,
                                       'contact': contact, 'add_category':add_category, 'order':order, 'orderItem':orderItem})
            else:
                return render(request, 'search_not_found.html')
        return render(request, 'profile.html',
                      context={'favorite': favorite, 'form': form, 'pass_form': password_form, 'cart': cart,
                               'comment': my_comment, 'products': product, 'add_form': add_product, 'user': user_list,
                               'blog': blog, 'add_blog': add_blog, 'ticket': ticket, 'contact': contact, 'add_category':add_category, 'orderItem':orderItem, 'order':order})
    else:
        ticket = Tickets.objects.filter(user=request.user)
        orderItem = get_list_or_404(OrderItem, user=request.user)
        order = get_list_or_404(Order, user=request.user)

        print(order)
        return render(request, 'profile.html',
                      context={'favorite': favorite, 'form': form, 'pass_form': password_form, 'cart': cart,
                               'comment': my_comment, 'ticket': ticket, 'orderItem':orderItem, 'order':order})


def updat_profile(requset):
    user = get_object_or_404(User, id=requset.user.id)
    form = ProfileForm(requset.POST, requset.FILES, instance=user)

    if form.is_valid():

        form.save()
        return redirect(reverse('accounts:profile_view'))
    else:
        print(form.errors)
    return redirect(reverse('accounts:profile_view'))


def change_password(request):
    user = get_object_or_404(User, id=request.user.id)
    form = ChangePassword(request.POST)
    if form.data['password1'] == form.data['password2']:
        user.password = make_password(form.data['password1'])
        user.save()
        return redirect(reverse('Home:HomeView'))

    return redirect(reverse('accounts:profile_view'))


def user_detail(request, pk):
    if request.user.is_superuser:
        user = get_object_or_404(User, id=pk)
        form = ProfileForm(instance=user)
        if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=user)

            if form.is_valid():
                print('dd')

                form.save()
                return redirect(reverse('accounts:profile_view'))
            else:
                print(form.errors)

        return render(request, 'account_cart.html', context={'UPform': form, 'user': user})


def delete_user(request, pk):
    if request.user.is_superuser:
        user = User.objects.get(id=pk)
        user.delete()
        return redirect(reverse('accounts:profile_view'))
    return redirect('blog:blog_list')

