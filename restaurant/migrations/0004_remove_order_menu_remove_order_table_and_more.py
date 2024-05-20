# Generated by Django 5.0.6 on 2024-05-20 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_reception_menu_order_waiter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
        migrations.RemoveField(
            model_name='waiter',
            name='orders',
        ),
        migrations.DeleteModel(
            name='Reception',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Waiter',
        ),
    ]
