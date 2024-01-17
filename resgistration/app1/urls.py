from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.SignupPage, name='signup'),
    path('login/',views.LoginPage, name='login'),
    path('logut/',views.LogoutPage, name='logout'),
    path('home/',views.HomePage,name='home'),
]
