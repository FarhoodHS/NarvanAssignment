from django.urls import path

from .views import fibonacci
from .api.views import FibonacciAPI

app_name = 'fibonacci'

urlpatterns = [
    path('', fibonacci, name='fibonacci'),
    path('api/', FibonacciAPI.as_view(), name='fibonacci_api'),
]
