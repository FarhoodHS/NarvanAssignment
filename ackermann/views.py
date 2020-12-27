from datetime import datetime
from django.contrib import messages
from django.shortcuts import render

from .forms import AckermannForm
from .utils import ackermann_func


def ackermann(request):
    if request.method == 'POST':
        form = AckermannForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            try:
                start_time = datetime.now()
                instance.result = ackermann_func(
                    form.cleaned_data['m'], form.cleaned_data['n'])
                instance.duration = datetime.now() - start_time
                # in order to save the object in the Database
                # instance.save()
            except RecursionError:
                messages.error(request,
                               'Sorry, this calculation is beyond limitations!')
            context = {
                'instance': instance
            }
            return render(request, 'ackermann.html', context)

    return render(request, 'ackermann.html')
