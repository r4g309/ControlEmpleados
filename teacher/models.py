from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

extra_hour = 40
value_extra_hour = 1.5
parafiscal = 0.09
bonus = 0.0833
severance = 0.0833
severance_interest = 00.1
vacation = 0.0417
health = 0.04
pension = 0.04


class Teacher(models.Model):
    nit = models.PositiveIntegerField(unique=True, validators=[MinLengthValidator(6), MaxLengthValidator(10)])
    name = models.TextField(max_length=40, validators=[MinLengthValidator(3)])
    work_hour = models.PositiveIntegerField()
    value_work = models.FloatField()

    def __str__(self):
        return self.name
