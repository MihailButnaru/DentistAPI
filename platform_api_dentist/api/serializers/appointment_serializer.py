from rest_framework.serializers import ModelSerializer
from platform_api_dentist.api.models import Appointments, AppointmentCard, Treatment


class AppointmentsSerializer(ModelSerializer):
    """Model for Appointments Serializer"""
    class Meta:
        model = Appointments
        fields = ['__all__']


class AppointmentCardSerializer(ModelSerializer):
    """Model for Appointment Card Serializer."""
    appointment_time = AppointmentsSerializer(many=True)

    class Meta:
        model = AppointmentCard
        fields = ['__all__']


class TreatmentSerializer(ModelSerializer):
    """Model for Treatment serializer"""

    class Meta:
        model = Treatment
        fields = ['__all__']
