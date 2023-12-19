from django.urls import path
from .views import login,signup, profile_view, logout,updat_profile, change_password,user_detail, delete_user

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('profile/', profile_view, name='profile_view'),
    path('updats_profile/', updat_profile, name="updats_profile"),
    path('change_password/', change_password, name="change_password"),
    path('<int:pk>/', user_detail, name="user_detail"),
    path('<int:pk>/delete', delete_user, name='delete_user'),
    # path('search', search_cod, name='search_cod'),




    
]