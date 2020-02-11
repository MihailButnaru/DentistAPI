from enum import Enum
from django.db import models

TREATMENT_TYPE = (
    ("Whitening", "Whitening"),
    ("Cleaning", "Cleaning"),
    ("Root Canal", "Root Canal"),
    ("Braces", "Braces"),
    ("Late Cancelation", "Late cancelation"),
    ("Filling", "Filling"),
)


class Treatment(models.Model):
    """Treatment representing a model."""

    treatment_type = models.CharField(max_length=50, choices=TREATMENT_TYPE)
    treatment_price = models.FloatField()
