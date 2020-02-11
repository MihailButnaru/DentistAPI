from django.test import TestCase
from datetime import datetime
from api.serializers.appointment_serializer import (
    TreatmentSerializer,
    AppointmentsSerializer,
    AppointmentCardSerializer,
)

fake_datetime = datetime.utcnow().isoformat()


class TestAppointmentsSerializer(TestCase):
    def setUp(self) -> None:
        self.appointment = {"location": "street number 1", "time": fake_datetime}
        self.appointment_card = {
            "name": "Tester",
            "address": "Tester London",
            "treatment_type": "Fever",
            "treatment_price": 100.0,
            "note": "test note",
            "dentist_note": "dentist note",
            "appointment_time": [
                {"location": "street number 1", "time": fake_datetime}
            ],
        }
        self.treatment = {"treatment_type": "Cleaning", "treatment_price": 100.0}

    def test_appointment_payload(self):
        """Test ensure that the appointment payload
        is valid by the serializer."""
        serializer = AppointmentsSerializer(data=self.appointment)

        self.assertTrue(serializer.is_valid())

    def test_appointment_card_payload(self):
        """Test ensures that the appointment card payload
        is valid by the serializer."""
        serializer = AppointmentCardSerializer(data=self.appointment_card)
        test = serializer.is_valid()

        self.assertTrue(serializer.is_valid())

    def test_treatment_payload(self):
        """Test ensures that the treatment payload
        is valid by the serializer."""
        serializer = TreatmentSerializer(data=self.treatment)

        self.assertTrue(serializer.is_valid())
