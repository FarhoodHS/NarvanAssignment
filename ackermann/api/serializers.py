from rest_framework.serializers import ModelSerializer

from ackermann.models import Ackermann


class AckermannSerializer(ModelSerializer):
    class Meta:
        model = Ackermann
        fields = ['m', 'n']
