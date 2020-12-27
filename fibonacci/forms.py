from django.forms import ModelForm

from .models import Fibonacci


class FibonacciForm(ModelForm):

    class Meta:
        model = Fibonacci
        fields = ['n']
