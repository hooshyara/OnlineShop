from django.contrib import admin
from .models import Blogs, Comments, Reply
from django_summernote.admin import SummernoteModelAdmin



# class BlogAdmin(admin.ModelAdmin):
#     list_display = ['title', 'user', 'datetime_created', 'is_active', ]


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog', 'user', 'datetime_created', ]


@admin.register(Reply)
class replyAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'datetime_created', ]


    
class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'
    login_template = 'blog/admin/login.html'


blog_site = BlogAdminArea(name='BlogAdmin')


class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = ['content']

admin.site.register(Blogs, BlogAdmin)