from .patient_model import Patient, Address
from .payment_model import Payment
from .dentist_model import DentistSpecialist
from .treatment_models import Treatment
from .appointment_card import Appointments, AppointmentCard

__all__ = [
    Patient,
    Address,
    Payment,
    Treatment,
    DentistSpecialist,
    AppointmentCard,
    Appointments
]
