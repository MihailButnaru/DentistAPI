from enum import Enum
from django.db import models


class TreatmentType(Enum):
    Whitening = "Whitening"
    Cleaning = "Cleaning"
    Root_Canal = "Root Canal"
    Braces = "Braces"
    Late_Cancelation = "Late Cancelation"
    Filling = "Filling"


class Treatment(models.Model):
    """Treatment representing a model."""
    treatment_type = models.CharField(max_length=50, choices=[(treatment, treatment.value) for treatment in TreatmentType])
    treatment_price = models.FloatField()
