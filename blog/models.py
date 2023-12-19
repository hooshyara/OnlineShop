from django.db import models
from django.urls import reverse
from accounts.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True)
    cover = models.ImageField(upload_to='blogs/', null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.id])


class Comments(models.Model):
    PRODUCT_STARS = [
        ('1', 'یک ستاره'),
        ('2', 'دو ستاره'),
        ('3', 'سه ستاره'),
        ('4', 'چهار ستاره'),
        ('5', 'پنج ستاره '),
    ]
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.CharField(max_length=100 ,null=True, choices=PRODUCT_STARS)
    text = models.TextField(null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse('Blog_List_View', args=[self.id])



class Reply(models.Model):
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name='reply')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

