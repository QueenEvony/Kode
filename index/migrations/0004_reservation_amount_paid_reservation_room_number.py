# Generated by Django 4.0.4 on 2022-06-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_reservation_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='amount_paid',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='room_number',
            field=models.IntegerField(default='0'),
        ),
    ]