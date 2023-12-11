"""deliver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer.views import Index, About, Order, OrderConfirmation, OrderPayConfirmation, Menu, MenuSearch, Restaurant, RestaurantSearch, RestaurantView, RestaurantOrderConfirmation, KeralaDishes, PunjabDishes, ContinentalDishes, Login, SignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('restaurant/', include('restaurant.urls')),
    path('', Index.as_view(), name='index'),
    path('about/', About.as_view(), name='about'),
    path('login/', Login.as_view(), name='login'),
    path('signup/', SignUp.as_view(), name = 'signup'),
    path('menu/',Menu.as_view(),name='menu'),
    path('restaurant',Restaurant.as_view(),name='restaurant'),
    path('menu/search/', MenuSearch.as_view(),name='menu-search'),
    path('restaurant/search/', RestaurantSearch.as_view(), name='restaurant-search'),
    path('restaurantitems/', RestaurantView.as_view(), name='restaurant-items'),
    path('KeralaDishes/', KeralaDishes.as_view(), name='KeralaDishes'),
    path('PunjabDishes/', PunjabDishes.as_view(), name='PunjabDishes'),
    path('ContinentalDishes/', ContinentalDishes.as_view(), name='ContinentalDishes'),
    path('restaurantorder-confirmation/<int:pk>', RestaurantOrderConfirmation.as_view(), name='restaurantorder-confirmation'),
    path('order/', Order.as_view(), name='order'),
    path('order-confirmation/<int:pk>',OrderConfirmation.as_view(),name='order-confirmation'),
    path('payment-confirmation/',OrderPayConfirmation.as_view(),name='payment-confirmation'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
