from django.urls import path
from .views import home_view

app_name = 'Home'
urlpatterns = [
    path('', home_view, name='HomeView'),

]
