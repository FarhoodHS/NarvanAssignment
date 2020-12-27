from datetime import datetime
from django.contrib import messages
from django.shortcuts import render

from .forms import FibonacciForm
from .utils import fibonacci_func


def fibonacci(request):
    if request.method == 'POST':
        form = FibonacciForm(request.POST or None)
        if form.is_valid():
            instance = form.save(commit=False)
            start_time = datetime.now()
            instance.result = fibonacci_func(form.cleaned_data['n'])
            instance.duration = datetime.now() - start_time
            # in order to save the object in the Database
            # instance.save()
        context = {
            'instance': instance
        }
        return render(request, 'fibonacci.html', context)

    return render(request, 'fibonacci.html')
