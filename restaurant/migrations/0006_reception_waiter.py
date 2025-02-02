# Generated by Django 5.0.6 on 2024-05-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reception',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('orders', models.ManyToManyField(related_name='waiters', to='restaurant.order')),
            ],
        ),
    ]
