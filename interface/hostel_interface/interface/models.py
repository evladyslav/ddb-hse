from django.db.models import (
    IntegerField,
    ForeignKey,
    UUIDField,
    CharField,
    BooleanField,
    SmallIntegerField,
    DateTimeField,
    TimeField,
    Model,
    CASCADE,
    DateField,
    BigAutoField,
)
from datetime import date


class PlaceType(Model):
    place_type_id = BigAutoField(primary_key=True)
    type = CharField(max_length=100)
    PRICE = SmallIntegerField()


class Places(Model):
    place_id = BigAutoField(primary_key=True)
    place_type_id = ForeignKey("PlaceType", on_delete=CASCADE)
    available = BooleanField(default=True)


class BookingStatus(Model):
    bk_id = BigAutoField(primary_key=True)
    status = CharField(max_length=1)
    description = CharField(max_length=100)


class Guests(Model):
    guest_id = BigAutoField(primary_key=True, unique=True)
    passport = CharField(max_length=10, unique=True)
    surname = CharField(max_length=20)
    name = CharField(max_length=20)
    fathername = CharField(max_length=20)
    gender = CharField(max_length=1)
    address = CharField(max_length=100)
    birthdate = DateField()
    phone_number = CharField(max_length=11)
    email = CharField(max_length=30)


class Bookings(Model):
    pb_id = BigAutoField(primary_key=True)
    arrival_date = DateField()
    checkout_date = DateField()
    money_total = IntegerField()
    bk_id = ForeignKey("BookingStatus", on_delete=CASCADE)
    guest_id = ForeignKey("Guests", on_delete=CASCADE)
    place_id = ForeignKey("Places", on_delete=CASCADE)


class Services(Model):
    service_id = BigAutoField(primary_key=True)
    price = SmallIntegerField()
    description = CharField(max_length=100)
