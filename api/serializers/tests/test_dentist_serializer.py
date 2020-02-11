from django.test import TestCase
from api.serializers.dentist_serializer import DentistSerializer


class TestDentistSpecialistSerializer(TestCase):
    def setUp(self) -> None:
        self.dentist = {
            "specialist_name": "Tester",
        }

    def test_correct_payload(self):
        """Test ensures that the specialist serializer
        validates the correct payload."""
        serializer = DentistSerializer(data=self.dentist)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["specialist_name"], "Tester")
