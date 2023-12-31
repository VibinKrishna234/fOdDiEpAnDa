# Generated by Django 4.2.6 on 2023-12-02 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0010_restaurantcategory_restaurantitems"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurantitems",
            name="city",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="restaurantitems",
            name="email",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="restaurantitems",
            name="is_paid",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="restaurantitems",
            name="is_shipped",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="restaurantitems",
            name="items",
            field=models.ManyToManyField(
                blank=True, related_name="rest_order", to="customer.menuitem"
            ),
        ),
        migrations.AddField(
            model_name="restaurantitems",
            name="state",
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name="restaurantitems",
            name="street",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name="restaurantitems",
            name="zip_code",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
