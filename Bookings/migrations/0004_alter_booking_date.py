# Generated by Django 4.1.3 on 2023-02-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookings', '0003_alter_booking_end_date_alter_booking_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
