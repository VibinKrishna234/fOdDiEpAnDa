from django.contrib import admin
from .models import MenuItem, Category, OrderModel, Restaurantmodel, RestaurantItems, RestaurantCategory

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(Restaurantmodel)
admin.site.register(RestaurantItems)
admin.site.register(RestaurantCategory)
