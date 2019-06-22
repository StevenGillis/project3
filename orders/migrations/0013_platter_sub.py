# Generated by Django 2.0.3 on 2019-06-22 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20190605_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platter',
            fields=[
                ('dish_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Dish')),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=10)),
            ],
            bases=('orders.dish',),
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('dish_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.Dish')),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], max_length=10)),
            ],
            bases=('orders.dish',),
        ),
    ]