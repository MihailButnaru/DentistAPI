from django.db import models
from .patient_model import Patient
from .treatment_models import Treatment
from .dentist_model import DentistSpecialist


class Appointments(models.Model):
    """Model representing appointments."""
    treatment_id = models.ForeignKey(Treatment, on_delete=models.CASCADE, verbose_name='treatment')
    appointment_time = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name='patient')


class AppointmentCard(models.Model):
    """Model representing an appointment card."""
    appointment = models.ForeignKey(Appointments, on_delete=models.CASCADE, verbose_name='appointment')
    name = models.CharField(max_length=15)
    address = models.CharField(max_length=15)
    treatment_type = models.CharField(max_length=15)
    treatment_price = models.FloatField()
    appointment_time = models.DateTimeField()
    note = models.CharField(max_length=50)
    dentist_note = models.CharField(max_length=50)
    refered_specialist = models.ForeignKey(DentistSpecialist, on_delete=models.CASCADE, verbose_name='refered_specialist')
