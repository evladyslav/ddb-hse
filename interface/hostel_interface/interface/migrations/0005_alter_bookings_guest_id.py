# Generated by Django 4.1.3 on 2022-12-07 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("interface", "0004_alter_bookings_guest_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookings",
            name="guest_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="interface.guests",
            ),
        ),
    ]
