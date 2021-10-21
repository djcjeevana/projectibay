
from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import login_request


from . import views



urlpatterns = [
    
    
    
    path('account/', views.account_update, name='account'),
    path('profile/', views.userprofile, name='userprofile'),
    
  
   
] 







