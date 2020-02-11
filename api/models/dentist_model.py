from django.db import models
from .treatment_models import Treatment


class DentistSpecialist(models.Model):
    """Model representing a dentist specialist."""

    specialist_name = models.CharField(max_length=15)
    treatment = models.ForeignKey(
        Treatment, on_delete=models.CASCADE, verbose_name="treatment"
    )
