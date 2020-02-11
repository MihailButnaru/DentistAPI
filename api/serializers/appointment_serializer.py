from rest_framework.serializers import ModelSerializer
from api.models import Appointments, AppointmentCard, Treatment


class AppointmentsSerializer(ModelSerializer):
    """Model for Appointments Serializer"""

    class Meta:
        model = Appointments
        fields = ["time", "location"]


class AppointmentCardSerializer(ModelSerializer):
    """Model for Appointment Card Serializer."""

    appointment_time = AppointmentsSerializer(many=True)

    class Meta:
        model = AppointmentCard
        fields = [
            "name",
            "address",
            "treatment_type",
            "treatment_price",
            "appointment_time",
            "note",
            "dentist_note",
        ]


class TreatmentSerializer(ModelSerializer):
    """Model for Treatment serializer"""

    class Meta:
        model = Treatment
        fields = ["treatment_type", "treatment_price"]
