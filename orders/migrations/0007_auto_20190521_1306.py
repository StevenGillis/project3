# Generated by Django 2.0.3 on 2019-05-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_pizza_toppings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='name',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
