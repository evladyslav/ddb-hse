# Generated by Django 4.1.3 on 2022-12-07 23:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("interface", "0005_alter_bookings_guest_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookings",
            name="money_total",
            field=models.IntegerField(),
        ),
    ]
