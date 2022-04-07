from django.core.exceptions import ValidationError
from django.core.validators import (
    MinLengthValidator,
    MinValueValidator,
    MaxValueValidator,
)
from django.db import models


class Teacher(models.Model):
    cc = models.PositiveIntegerField(
        unique=True,
        validators=[MinValueValidator(10000000), MaxValueValidator(9999999999)],
    )
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    work_hour = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    value_work = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return self.name

    @staticmethod
    def calculate_extras_hours(work_hour, value_hour, extra_hour, value_extra_hour):
        if work_hour >= extra_hour:
            extras = work_hour - extra_hour
            return extras * (value_hour * value_extra_hour)
        return 0

    @staticmethod
    def calculate_parafiscal_enterprise(gross_value, extras, parafiscal_enterprise):
        return (gross_value + extras) * parafiscal_enterprise

    @staticmethod
    def calculate_parafiscal_worker(gross_value, extras, parafiscal_worker):
        return (gross_value + extras) * parafiscal_worker

    @staticmethod
    def calculate_bonus(gross_balance, bonus):
        return gross_balance * bonus

    @staticmethod
    def calculate_severance(gross_balance, severance):
        return gross_balance * severance

    @staticmethod
    def calculate_severance_interest(severance, severance_interest):
        return severance * severance_interest

    @staticmethod
    def calculate_vacation(gross_balance, vacation):
        return gross_balance * vacation

    @staticmethod
    def calculate_health(gross_balance, health):
        return gross_balance * health

    @staticmethod
    def calculate_pension(gross_balance, pension):
        return gross_balance * pension
