from rest_framework.serializers import ModelSerializer
from platform_api_dentist.api.models import Patient, Address, Payment


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
