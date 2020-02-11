from enum import Enum
from django.db import models
from django.core.validators import RegexValidator
from .patient_model import Patient

PAYMENT_METHODS = (("Cash", "Cash"), ("Cheque", "Cheque"))


class Payment(models.Model):
    """Model representing a payment."""

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name="payment"
    )
    lodgement_date = models.DateTimeField()
    payment_method = models.CharField(max_length=15, choices=PAYMENT_METHODS)
    sort_code = models.CharField(
        max_length=6,
        validators=[
            RegexValidator(
                regex=r"^[0-9]+$",
                code="Invalid sort code",
                message="Invalid sort code",
            )
        ],
    )
    account_number = models.CharField(
        max_length=8,
        validators=[
            RegexValidator(
                regex=r"^[0-9]+$",
                code="Invalid account number",
                message="Invalid account number",
            )
        ],
    )
    bank_name = models.CharField(max_length=15)
    pay = models.FloatField()
