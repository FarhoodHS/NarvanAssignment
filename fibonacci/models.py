from django.db import models


class Fibonacci(models.Model):

    n = models.PositiveIntegerField()
    result = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
