# Generated by Django 5.0.6 on 2024-07-06 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_delete_random'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='email',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='phone',
        ),
    ]
