# Generated by Django 4.2.6 on 2023-12-03 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0015_category_restaurant"),
    ]

    operations = [
        migrations.RemoveField(model_name="restaurantitems", name="city",),
        migrations.RemoveField(model_name="restaurantitems", name="email",),
        migrations.RemoveField(model_name="restaurantitems", name="is_paid",),
        migrations.RemoveField(model_name="restaurantitems", name="is_shipped",),
        migrations.RemoveField(model_name="restaurantitems", name="items",),
        migrations.RemoveField(model_name="restaurantitems", name="state",),
        migrations.RemoveField(model_name="restaurantitems", name="street",),
        migrations.RemoveField(model_name="restaurantitems", name="zip_code",),
    ]
