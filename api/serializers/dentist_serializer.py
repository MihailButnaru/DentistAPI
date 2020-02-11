from rest_framework.serializers import ModelSerializer
from api.models.dentist_model import DentistSpecialist


class DentistSerializer(ModelSerializer):
    """Model for dentist serializer."""

    class Meta:
        model = DentistSpecialist
        fields = ["specialist_name"]
