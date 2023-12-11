import json

from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import MenuItem, Category, OrderModel, Restaurantmodel, RestaurantItems
from django.core.mail import send_mail



class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/login.html')

class SignUp(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/signup.html')

class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/about.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Kerala_Dishes = MenuItem.objects.filter(category__name__contains='Kerala_Dishes')
        Andhra_Dishes = MenuItem.objects.filter(category__name__contains='Andhra Dishes')
        Tamil_Dishes = MenuItem.objects.filter(category__name__contains='Tamil Dishes')
        Hot_Drinks = MenuItem.objects.filter(category__name__contains='Hot_Drinks')
        Punjab_Dishes = MenuItem.objects.filter(category__name__contains='Punjab_Dishes')
        Continental_Cuisines = RestaurantItems.objects.filter(category__name__contains='Continental_Cuisines')
        context = {
            'Kerala_Dishes': Kerala_Dishes,
            'Andhra_Dishes': Andhra_Dishes,
            'Tamil_Dishes': Tamil_Dishes,
            'Hot_Drinks': Hot_Drinks,
            'Punjab_Dishes': Punjab_Dishes,
            'Continental_Cuisines': Continental_Cuisines,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)

            # After everything is done, send confirmation email to the user
        # body = ('Thank you for your Order! Your food is being made and will be delivered soon!\n'
        #         f'Your total: {price}\n'
        #         'Thank you again for your order!')
        # send_mail(
        #     'Thank You for your order!',
        #     body,
        #     'example@example.com',
        #     [email],
        #     fail_silently=False
        # )
        context = {
            'items': order_items['items'],
            'price': price

        }
        #return render(request, 'customer/order_confirmation.html', context)
        return redirect('order-confirmation',pk=order.pk)


class OrderConfirmation(View):
    def get(self,request, pk, *args,**kwargs):
        order =OrderModel.objects.get(pk = pk)
        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'customer/order_confirmation.html',context)
    def post(self,request,pk,*args,**kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()
        return redirect('payment-confirmation')
class OrderPayConfirmation(View):
    def get(self,request,*args,**kwargs):
        return render(request,'customer/order_pay_confirmation.html')

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }
        return render(request, 'customer/menu.html', context)

class MenuSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        menu_items = MenuItem.objects.filter(
            Q(name__icontains=query) |
            Q(price__icontains=query) |
            Q(description__icontains=query)
        )

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)

class RestaurantSearch(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get("q")

        name = Restaurantmodel.objects.filter(
            Q(restaurant_name__icontains=query) |
            Q(address__icontains=query)

        )

        context = {
            'name': name
        }

        return render(request, 'customer/restaurant.html', context)

class Restaurant(View):
    def get(self, request, *args, **kwargs):
        name = Restaurantmodel.objects.all()

        context = {
            'name': name
        }
        return render(request, 'customer/restaurant.html', context)

class RestaurantView(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Kerala_Dishes = RestaurantItems.objects.filter(category__name__contains='Kerala_Dishes')
        Andhra_Dishes = RestaurantItems.objects.filter(category__name__contains='Andhra Dishes')
        Tamil_Dishes = RestaurantItems.objects.filter(category__name__contains='Tamil Dishes')
        Hot_Drinks = RestaurantItems.objects.filter(category__name__contains='Hot_Drinks')
        Punjab_Dishes = RestaurantItems.objects.filter(category__name__contains='Punjab_Dishes')
        Continental_Cuisines = RestaurantItems.objects.filter(category__name__contains='Continental_Cuisines')
        context = {
            'Kerala_Dishes': Kerala_Dishes,
            'Andhra_Dishes': Andhra_Dishes,
            'Tamil_Dishes': Tamil_Dishes,
            'Hot_Drinks': Hot_Drinks,
            'Punjab_Dishes': Punjab_Dishes,
            'Continental_Cuisines': Continental_Cuisines,
        }
        return render(request, 'customer/restaurant_items.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            restaurant_items = RestaurantItems.objects.get(pk__contains=int(item))
            item_data = {
                'id': restaurant_items.pk,
                'name': restaurant_items.name,
                'price': restaurant_items.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            rest_order= RestaurantItems.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            rest_order.items.add(*item_ids)

            # After everything is done, send confirmation email to the user
        # body = ('Thank you for your Order! Your food is being made and will be delivered soon!\n'
        #         f'Your total: {price}\n'
        #         'Thank you again for your order!')
        # send_mail(
        #     'Thank You for your order!',
        #     body,
        #     'example@example.com',
        #     [email],
        #     fail_silently=False
        # )
        context = {
            'items': order_items['items'],
            'price': price

        }
        # return render(request, 'customer/restaurantorder_confirmation.html', context)
        return redirect('restaurantorder-confirmation',pk=rest_order.pk)

# class dish_list(View):
#     def get(self, request, restaurant_id):
#         category_items = RestaurantItems.objects.filter(restaurant_id=restaurant_id)
#         return render(request, 'customer/restaurant_items.html', {'category_items': category_items})

class RestaurantOrderConfirmation(View):
    def get(self,request, pk, *args,**kwargs):
        order =RestaurantItems.objects.get(pk = pk)
        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'customer/restaurantorder_confirmation.html',context)
    def post(self,request,pk,*args,**kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = RestaurantItems.objects.get(pk=pk)
            order.is_paid = True
            order.save()
        return redirect('payment-confirmation')

class KeralaDishes(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Kerala_Dishes = MenuItem.objects.filter(category__name__contains='Kerala_Dishes')
        context = {
            'Kerala_Dishes': Kerala_Dishes,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price

        }
        #return render(request, 'customer/order_confirmation.html', context)
        return redirect('order-confirmation',pk=order.pk)

class AndhraDishes(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Andhra_Dishes = MenuItem.objects.filter(category__name__contains='Andhra Dishes')

        context = {
            'Andhra_Dishes': Andhra_Dishes,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price

        }
        # return render(request, 'customer/order_confirmation.html', context)
        return redirect('order-confirmation', pk=order.pk)

class TamilDishes(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Tamil_Dishes = MenuItem.objects.filter(category__name__contains='Tamil Dishes')
        context = {
            'Tamil_Dishes': Tamil_Dishes,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)

            # After everything is done, send confirmation email to the user
        # body = ('Thank you for your Order! Your food is being made and will be delivered soon!\n'
        #         f'Your total: {price}\n'
        #         'Thank you again for your order!')
        # send_mail(
        #     'Thank You for your order!',
        #     body,
        #     'example@example.com',
        #     [email],
        #     fail_silently=False
        # )
        context = {
            'items': order_items['items'],
            'price': price

        }
        # return render(request, 'customer/order_confirmation.html', context)
        return redirect('order-confirmation', pk=order.pk)

class HotDrinks(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Hot_Drinks = MenuItem.objects.filter(category__name__contains='Hot_Drinks')
        context = {
            'Hot_Drinks': Hot_Drinks,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price

        }
        # return render(request, 'customer/order_confirmation.html', context)
        return redirect('order-confirmation', pk=order.pk)

class PunjabDishes(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Punjab_Dishes = MenuItem.objects.filter(category__name__contains='Punjab_Dishes')
        context = {
            'Punjab_Dishes': Punjab_Dishes,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price

        }
        # return render(request, 'customer/order_confirmation.html', context)
        return redirect('order-confirmation', pk=order.pk)

class ContinentalDishes(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        Continental_Cuisines = RestaurantItems.objects.filter(category__name__contains='Continental_Cuisines')
        context = {
            'Continental_Cuisines': Continental_Cuisines,
        }
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        street = request.POST.get('street')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip')
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price,

            }
            order_items['items'].append(item_data)
        price = 0
        item_ids = []
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

            order = OrderModel.objects.create(
                price=price,
                name=name,
                email=email,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code
            )
            order.items.add(*item_ids)
        context = {
            'items': order_items['items'],
            'price': price

        }
        #return render(request, 'customer/order_confirmation.html', context)
        return redirect('order-confirmation',pk=order.pk)







