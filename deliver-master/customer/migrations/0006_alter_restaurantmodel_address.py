# Generated by Django 4.2.6 on 2023-11-30 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0005_restaurantmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurantmodel", name="address", field=models.TextField(),
        ),
    ]