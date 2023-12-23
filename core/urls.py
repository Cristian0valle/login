from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name = 'products'),
    path('logout/', views.exit, name = 'exit'), 
    path('register/', views.register, name = 'register')
]
