from django.shortcuts import render, redirect, reverse,get_object_or_404
from .models import Blogs, Comments
from django.views import generic
from django.urls import reverse_lazy
from .forms import CommentForm, ReplyForm, AddBlogForm
from accounts.models import User


def blog_list_view(request):
    user = User()
    blog_list = Blogs.objects.filter(is_active=True)
    return render(request, 'blog_list.html', context={'blogs':blog_list, 'user':user})

class BlogDetailView(generic.DetailView):
    model = Blogs
    template_name = 'blog_detail.html'
    context_object_name = 'blog'


class CommentCreatView(generic.View):
    model = Comments
    form = CommentForm
    template_name = 'comment/comment_create.html'

    def get(self, request, id):
        form = self.form()
        context = {'form': form}
        if request.user.is_authenticated:
            return render(request, self.template_name, context)
        return redirect(reverse('accounts:login'))

    def post(self, request, id):
        form = self.form(request.POST)
        blog = Blogs.objects.get(id=id)
        if form.is_valid():
            comment = self.model.objects.create(
                blog=blog,
                user= request.user,
                text=form.cleaned_data['text']
            )
            comment.save()
            return redirect('blog:blog_list')
        

        
def add_blog(request):
    if request.user.is_superuser:
        
        if request.method == "POST":
            print('ddd')
            form = AddBlogForm(request.POST, request.FILES)
            if form.is_valid():
                blog = Blogs.objects.create(
                    user = request.user,
                    title = form.data['title'],
                    content = form.data['content'],
                    is_active = True if form.data['is_active'] else False
                )
                blog.save()
                return redirect('accounts:profile_view')
            else:
                print(form.errors)
        return redirect('blog:blog_list')


def delete_blog_view(request, blog_id):
    if request.user.is_superuser:
        blog = Blogs.objects.get(id=blog_id)
        blog.delete()
        return redirect(reverse('accounts:profile_view'))
    return redirect('blog:blog_list')
    

def update_blog(request, pk):
    if request.user.is_superuser:
        blog = get_object_or_404(Blogs, id=pk)
        form = AddBlogForm(instance=blog)
        if request.method == "POST":
            form = AddBlogForm(request.POST , request.FILES ,instance=blog)
            if form.is_valid():
                form.save()
                return redirect(reverse('accounts:profile_view'))
            else:
                print(form.errors)
        return render(request, 'blog_update.html', context={'UPform':form, 'blog':blog})
            
