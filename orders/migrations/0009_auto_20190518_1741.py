# Generated by Django 2.0.3 on 2019-05-18 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20190518_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buyer_ID',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='boughtby', to='orders.Buyer'),
        ),
    ]