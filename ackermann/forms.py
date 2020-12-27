from django.forms import ModelForm

from .models import Ackermann


class AckermannForm(ModelForm):

    class Meta:
        model = Ackermann
        fields = ['m', 'n']
