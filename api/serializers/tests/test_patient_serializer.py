from django.test import TestCase
from api.serializers.patient_serializer import PatientSerializer


class TestPatientSerializer(TestCase):
    def setUp(self) -> None:
        pass

    def test_correct_payload(self):
        """Test ensures that the correct payload
        is validated by the serializer."""
        pass
