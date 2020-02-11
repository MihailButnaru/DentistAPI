"""Patient model"""
from enum import Enum

from django.core.validators import RegexValidator
from django.db import models


GENRE = (("M", "Masculine"), ("F", "Feminine"))

PAYMENT_TYPES = (
    ("Direct Debit", "Direct Debit"),
    ("Pending confirmation", "Pending confirmation"),
    ("One time Payment", "One time Payment"),
    ("Installments", "Installments"),
)


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
    genre = models.CharField(max_length=15, choices=GENRE)
    date_of_birth = models.DateTimeField()
    email = models.CharField(max_length=50)
    outstanding_balance = models.FloatField()
    next_appoitment = models.DateTimeField(null=True)
    app_id = models.IntegerField()  # Foreign Key
    payment_type = models.CharField(max_length=50, choices=PAYMENT_TYPES, null=True,)


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
