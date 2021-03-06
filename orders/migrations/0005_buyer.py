# Generated by Django 2.0.3 on 2019-05-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('order_ID', models.ManyToManyField(blank=True, related_name='ordered', to='orders.Order')),
            ],
        ),
    ]
