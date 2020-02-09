import datetime
from django.test import TestCase
from api.models import Patient
from django.core.exceptions import ValidationError

fake_date = datetime.datetime(2000, 1, 10)


class TestPatientModel(TestCase):
    def setUp(self) -> None:
        Patient.objects.create(
            first_name="Tester",
            last_name="Smith",
            genre="M",
            date_of_birth=fake_date,
            email="testers@uk",
            outstanding_balance=0.0,
            next_appoitment=fake_date,
            app_id=1,
            payment_type="Direct_Debit",
        )

    def test_create_patient_object(self):
        """Test ensures that a patient object is created."""
        patient = Patient.objects.get(first_name="Tester")

        self.assertEqual(patient.first_name, "Tester")
        self.assertEqual(patient.genre, "M")
        self.assertEqual(patient.payment_type, "Direct_Debit")

    def test_invalid_payload_create_object(self):
        """Test ensures that a invalid payload is validated."""
        patient = Patient.objects.create(
            first_name="Tester1",
            last_name="Smith",
            genre="M",
            date_of_birth=fake_date,
            email="tester@uk",
            outstanding_balance=0.0,
            app_id=1,
            payment_type="Direct_Debit",
        )

        with self.assertRaises(ValidationError):
            patient.full_clean()
