from datetime import datetime
from django.test import TestCase
from api.serializers.patient_serializer import (
    PatientSerializer,
    AddressSerializer,
    PaymentSerializer,
)

fake_date = datetime.utcnow().isoformat()


class TestPatientSerializer(TestCase):
    def setUp(self) -> None:
        self.patient = {
            "first_name": "Tester",
            "last_name": "Smith",
            "genre": "M",
            "date_of_birth": fake_date,
            "email": "testers@hotmail.com",
            "outstanding_balance": 10.0,
            "app_id": 1,
            "payment_type": "Direct Debit",
            "address": {
                "address_line_one": "London",
                "address_line_two": "London Street",
                "postcode": "E1",
                "city": "London",
                "town": "London",
                "county": "L",
            },
        }
        self.address = {
            "address_line_one": "London",
            "address_line_two": "London Street",
            "postcode": "E1",
            "city": "London",
            "town": "London",
            "county": "L",
        }
        self.payment = {
            "lodgement_date": fake_date,
            "payment_method": "Cash",
            "sort_code": "010111",
            "account_number": "68661112",
            "bank_name": "Natwest",
            "pay": 100.0,
        }

    def test_correct_payload(self):
        """Test ensures that the correct payload
        is validated by the serializer."""
        serializer = PatientSerializer(data=self.patient)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["first_name"], "Tester")

    def test_correct_address_serializer(self):
        """Test ensures that the correct payload is
        validated by the address serializer."""
        serializer = AddressSerializer(data=self.address)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["address_line_one"], "London")

    def test_correct_payment_serializer(self):
        """Test ensures that the correct payload is
        validated by the payment serializer."""
        serializer = PaymentSerializer(data=self.payment)

        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.validated_data["sort_code"], "010111")

    def test_invalid_sort_code_payment_serializer(self):
        """Test ensures that a valid sort code is
        validated by the payment serializer."""
        payment = {
            "lodgement_date": fake_date,
            "payment_method": "Cash",
            "sort_code": "01as11",
            "account_number": "68661112",
            "bank_name": "Natwest",
            "pay": 100.0,
        }
        serializer = PaymentSerializer(data=payment)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors["sort_code"][0], "Invalid sort code")

    def test_invalid_account_number_payment_serializer(self):
        """Test ensures that a valid account number is
        validated by the payment serializer."""
        payment = {
            "lodgement_date": fake_date,
            "payment_method": "Cash",
            "sort_code": "010101",
            "account_number": "686sd112",
            "bank_name": "Natwest",
            "pay": 100.0,
        }
        serializer = PaymentSerializer(data=payment)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["account_number"][0], "Invalid account number"
        )
