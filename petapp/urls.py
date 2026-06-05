from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('dogs/', views.dogs, name='dogs'),
    path('cats/', views.cats, name='cats'),
    path('smallpets/', views.smallpets, name='smallpets'),
    path('breed/', views.breed, name='breed'),
    path('consultvet/', views.consultvet, name='consultvet'),
    path('likes/', views.likes, name='likes'),
    path('cart/', views.cart, name='cart'),
    path('signin/', views.signin, name='signin'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', views.order, name='order'),
    path('tracking/', views.tracking, name='tracking'),
]