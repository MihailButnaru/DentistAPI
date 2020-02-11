from rest_framework.serializers import ModelSerializer
from api.models.patient_model import Patient, Address
from api.models.payment_model import Payment


class AddressSerializer(ModelSerializer):
    """Model serializer for address."""
    class Meta:
        model = Address
        fields = ['__all__']


class PatientSerializer(ModelSerializer):
    """Model serializer for patient."""
    address = AddressSerializer(many=False)

    class Meta:
        model = Patient
        fields = ['__all__']


class PaymentSerializer(ModelSerializer):
    """Model serializer for payment"""
    class Meta:
        model = Payment
        fields = ['__all__']
