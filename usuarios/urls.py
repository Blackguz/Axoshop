from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegistrarView.as_view(), name='register'),
]
