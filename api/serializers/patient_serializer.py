from rest_framework.serializers import ModelSerializer
from api.models.patient_model import Patient, Address
from api.models.payment_model import Payment


class AddressSerializer(ModelSerializer):
    """Model serializer for address."""

    class Meta:
        model = Address
        fields = [
            "address_line_one",
            "address_line_two",
            "postcode",
            "city",
            "town",
            "county",
        ]


class PatientSerializer(ModelSerializer):
    """Model serializer for patient."""

    address = AddressSerializer(many=False)

    class Meta:
        model = Patient
        fields = [
            "first_name",
            "last_name",
            "genre",
            "date_of_birth",
            "email",
            "outstanding_balance",
            "app_id",
            "payment_type",
            "address",
        ]


class PaymentSerializer(ModelSerializer):
    """Model serializer for payment"""

    class Meta:
        model = Payment
        fields = [
            "lodgement_date",
            "payment_method",
            "sort_code",
            "account_number",
            "bank_name",
            "pay",
        ]
