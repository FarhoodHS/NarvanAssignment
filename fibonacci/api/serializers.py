from rest_framework.serializers import ModelSerializer

from fibonacci.models import Fibonacci


class FibonacciSerializer(ModelSerializer):
    class Meta:
        model = Fibonacci
        fields = ['n']
