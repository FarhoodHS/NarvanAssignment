from django.urls import path

from .views import ackermann
from .api.views import AckermannAPI

app_name = 'ackermann'

urlpatterns = [
    path('', ackermann, name='ackermann'),
    path('api/', AckermannAPI.as_view(), name='ackermann_api'),
]
