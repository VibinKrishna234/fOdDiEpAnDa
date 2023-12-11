# Generated by Django 4.2.6 on 2023-12-02 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0013_dish"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="category",
            field=models.ManyToManyField(
                related_name="categories", to="customer.category"
            ),
        ),
    ]