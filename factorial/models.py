from django.db import models


class Factorial(models.Model):

    n = models.PositiveIntegerField()
    result = models.IntegerField()
