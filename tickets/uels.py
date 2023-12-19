from django.urls import path
from .views import ticket_view, ticket_detail, ticket_message, delete_ticket



app_name = 'ticket'
urlpatterns = [
    path('', ticket_view, name='ticket'),
    path('<int:pk>', ticket_detail, name='ticket_detail'),
    path('ticket_message/<int:id>', ticket_message, name='ticket_message'),
    path('delete_ticket/<int:id>', delete_ticket, name='delete_ticket')


    
]
