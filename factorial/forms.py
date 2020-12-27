from django.forms import ModelForm

from .models import Factorial


class FactorialForm(ModelForm):

    class Meta:
        model = Factorial
        fields = ['n']
