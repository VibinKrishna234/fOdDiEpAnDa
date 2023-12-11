from django.db import models


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('Category', related_name='item')

    def __str__(self):
        return self.name

class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'


class Restaurantmodel(models.Model):
    restaurant_name = models.CharField(max_length=100)
    address = models.TextField()
    image = models.ImageField(upload_to='menu_images')

    def __str__(self):
        return self.restaurant_name

class Category(models.Model):
    name = models.CharField(max_length=100)
    restaurant = models.ManyToManyField(Restaurantmodel, related_name='restaurants')
    def __str__(self):
        return self.name

# class Dish(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)
#     restaurant = models.ForeignKey(Restaurantmodel, on_delete=models.CASCADE)
#     category = models.ManyToManyField(Category, related_name='categories')
#
#     def __str__(self):
#         return self.name

class RestaurantCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class RestaurantItems(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ManyToManyField('RestaurantCategory', related_name='item')
    items = models.ManyToManyField('RestaurantItems', related_name='rest_order', blank=True)
    email = models.CharField(max_length=50, blank=True)
    street = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=15, blank=True)
    zip_code = models.IntegerField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models.BooleanField(default=False)
