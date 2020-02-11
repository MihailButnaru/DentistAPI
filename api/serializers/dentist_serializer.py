from rest_framework.serializers import ModelSerializer
from api import DentistSpecialist


class DentistSerializer(ModelSerializer):
    """Model for dentist serializer."""
    class Meta:
        model = DentistSpecialist
        fields = ['__all__']
