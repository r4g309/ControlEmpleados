from django.test import TestCase
from teacher.models import Teacher

extra_hour = 40
value_extra_hour = 1.5
parafiscal = 0.09
bonus = 0.0833
severance = 0.0833
severance_interest = 0.01
vacation = 0.0417
health = 0.04
pension = 0.04


class TeacherTestCase(TestCase):
    def setUp(self):
        Teacher.objects.create(cc=1077123552, name="Persona 1", work_hour=10, value_work=1)
        Teacher.objects.create(cc=1099999999, name="Persona 2", work_hour=50, value_work=13)

    def test_check_extra_hours(self):
        """Si las horas extras son menores a extra_hour devolver 0"""
        teacher1 = Teacher.objects.get(cc=1077123552)
        teacher2 = Teacher.objects.get(cc=1099999999)
        self.assertEqual(
            Teacher.calculate_extras_hours(teacher1.work_hour, teacher1.value_work, extra_hour, value_extra_hour), 0)

        self.assertEqual(
            Teacher.calculate_extras_hours(teacher2.work_hour, teacher2.value_work, extra_hour, value_extra_hour), 195)

