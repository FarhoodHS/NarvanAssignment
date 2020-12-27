from datetime import datetime
from django.contrib import messages
from django.shortcuts import render

from .forms import FactorialForm
from .utils import factorial_func


def factorial(request):
    if request.method == 'POST':
        form = FactorialForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            start_time = datetime.now()
            instance.result = factorial_func(form.cleaned_data['n'])
            instance.duration = datetime.now() - start_time
            # in order to save the object in the Database
            # instance.save()
        context = {
            'instance': instance
        }
        return render(request, 'factorial.html', context)

    return render(request, 'factorial.html')
