from django.db import models


class Ackermann(models.Model):

    m = models.PositiveIntegerField()
    n = models.PositiveIntegerField()
    result = models.IntegerField()
