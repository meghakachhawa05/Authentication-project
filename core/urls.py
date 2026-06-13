from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='user_login'),
    path('forgot-password/', views.forgot_passwordView, name='forgot_password'),
    path('logout/', views.LogoutView, name='logout'),
    path('password-reset-sent/<str:reset_id>/', views.Password_Reset_Sent, name='password_reset_sent'),
    path('reset-password/<str:reset_id>/', views.Reset_Password, name='reset_password'),

]
