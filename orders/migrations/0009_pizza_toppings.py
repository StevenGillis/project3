# Generated by Django 2.0.3 on 2019-05-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190521_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='toppings',
            field=models.CharField(choices=[('one', 'One'), ('two', 'two'), ('three', 'three'), ('Cheese', 'Cheese')], default='One', max_length=10),
            preserve_default=False,
        ),
    ]
