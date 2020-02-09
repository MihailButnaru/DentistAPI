"""Patient model"""
from enum import Enum

from django.core.validators import RegexValidator
from django.db import models


class Genre(Enum):
    M = "masculine"
    F = "feminine"


class PaymentTypes(Enum):
    Pending_confirmation = "Pending_confirmation"
    Direct_Debit = "Direct Debit"
    One_time = "One-time Payment"
    Installments = "Installments"


class Patient(models.Model):
    """Model representing a patient."""

    first_name = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z- ]+$",
                code="Invalid first name",
                message="First name must not contain any symbols!",
            )
        ],
    )
    last_name = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^[a-zA-Z- ]+$",
                code="Invalid last name",
                message="Last name must not contain any symbols!",
            )
        ],
    )
    genre = models.CharField(
        max_length=15, choices=[(genre, genre.value) for genre in Genre]
    )
    date_of_birth = models.DateTimeField()
    email = models.CharField(max_length=15)
    outstanding_balance = models.FloatField()
    next_appointment = models.DateTimeField(null=True)
    payment_type = models.CharField(
        max_length=50,
        choices=[(payment, payment.value) for payment in PaymentTypes],
        null=True,
    )


class Address(models.Model):
    """Model representing an address."""

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name="address"
    )
    address_line_one = models.CharField(max_length=50)
    address_line_two = models.CharField(max_length=50)
    postcode = models.CharField(max_length=50)
    city = models.CharField(max_length=15)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=15)
