from rest_framework.serializers import ModelSerializer

from factorial.models import Factorial


class FactorialSerializer(ModelSerializer):
    class Meta:
        model = Factorial
        fields = ['n']
