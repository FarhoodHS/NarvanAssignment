from django.urls import path

from .views import factorial
from .api.views import FactorialAPI

app_name = 'factorial'

urlpatterns = [
    path('', factorial, name='factorial'),
    path('api/', FactorialAPI.as_view(), name='factorial_api'),
]
