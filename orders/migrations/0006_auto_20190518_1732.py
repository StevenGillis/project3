# Generated by Django 2.0.3 on 2019-05-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='time',
            field=models.CharField(default='now', max_length=64),
        ),
        migrations.AddField(
            model_name='order',
            name='totalamount',
            field=models.CharField(default=0, max_length=64),
        ),
    ]