from django.urls import path
from .views import blog_list_view, BlogDetailView, CommentCreatView, delete_blog_view, update_blog, add_blog
app_name = 'blog'
urlpatterns = [
    path('', blog_list_view, name='blog_list'),
    path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:id>/comment', CommentCreatView.as_view(), name='comment_create'),
    path('update/<int:pk>', update_blog, name='update_blog'),
    path('delete/<int:blog_id>', delete_blog_view, name='delete_blog'),
    path('add_blog', add_blog, name='add_blog'),


]