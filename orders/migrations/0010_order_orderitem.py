# Generated by Django 2.0.3 on 2019-05-22 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_pizza_toppings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
