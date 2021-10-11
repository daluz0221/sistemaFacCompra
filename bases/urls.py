from django.urls import path
from django.contrib.auth import views as av

from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', av.LoginView.as_view(template_name='bases/login.html'), name='login'),
    path('logout/', av.LogoutView.as_view(template_name='bases/login.html'), name='logout'),
]