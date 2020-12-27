from django.contrib import admin
from django.urls import path, include
from .views import home

app_name = 'home'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home, name='homepage'),
    path('fibonacci/', include('fibonacci.urls')),
    path('ackermann/', include('ackermann.urls')),
    path('factorial/', include('factorial.urls')),
]
