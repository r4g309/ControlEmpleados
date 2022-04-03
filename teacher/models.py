from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models


def validator_nit(value):
    if not 10000000 <= value <= 9999999999:
        raise ValidationError(
            "escriba bien el numero de la cédula",
            params={"value": value},
        )


extra_hour = 40
value_extra_hour = 1.5
parafiscal = 0.09
bonus = 0.0833
severance = 0.0833
severance_interest = 0.01
vacation = 0.0417
health = 0.04
pension = 0.04


class Teacher(models.Model):
    nit = models.PositiveIntegerField(unique=True, validators=[validator_nit])
    name = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    work_hour = models.PositiveIntegerField()
    value_work = models.FloatField()

    def __str__(self):
        return self.name

    @staticmethod
    def calculate_extras_hours(work_hour, value_hour, extra_hour, value_extra_hour):
        gross_balance = work_hour * value_hour
        if work_hour >= extra_hour:
            extras = extra_hour - work_hour
            gross_balance += extras * (value_hour * value_extra_hour)
        return gross_balance

    @staticmethod
    def calculate_parafiscals(gross_balace, parafiscal):
        return gross_balace * parafiscal

    @staticmethod
    def calculate_bonus(gross_balance, bonus):
        return gross_balance * bonus

    @staticmethod
    def calculate_severance(gross_balance, severance):
        return gross_balance * severance

    @staticmethod
    def calculate_severance_interest(gross_balance, severance_interest):
        return gross_balance * severance_interest

    @staticmethod
    def calculate_vacation(gross_balance, vacation):
        return gross_balance * vacation

    @staticmethod
    def calculate_health(gross_balance, health):
        return gross_balance * health

    @staticmethod
    def calculate_pension(gross_balance, pension):
        return gross_balance * pension
