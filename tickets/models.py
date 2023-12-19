from django.db import models
from accounts.models import User
from django.utils import timezone
import random
import string


def generate_unic_code():
    cod_length = 6
    characters = string.ascii_letters + string.digits

    while(True):
        code = ''.join(random.choice(characters) for _ in range(cod_length)) 
        
        if not Tickets.objects.filter(code=code).exists():
            return code
            





class Tickets(models.Model):
    PRIORITY = [
        ('1', ' زیاد'),
        ('2', 'متوسط '),
        ('3', 'کم '),
        
    ]
    STATUS = [
        ('1', ' پاسغ داده شده'),
        ('2', 'پاسخ داده نشده'), 
        ('3', '  در حال برسی'),        

    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    code = models.CharField(max_length=6, unique=True, default=generate_unic_code, null=True)
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=timezone.now, null=True)
    priority = models.CharField(max_length=100, choices=PRIORITY)
    status = models.CharField(max_length=100, choices=STATUS, default='3')
    active  = models.BooleanField(default=True)



class TicketMessage(models.Model):
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    file = models.FileField(blank=True)
    date = models.DateField(auto_now_add=timezone.now, null=True)
    

