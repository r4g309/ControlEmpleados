# Generated by Django 4.0.3 on 2022-04-03 23:57

import django.core.validators
from django.db import migrations, models
import teacher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc', models.PositiveIntegerField(unique=True, validators=[teacher.models.validator_cc])),
                ('name', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(3)])),
                ('work_hour', models.PositiveIntegerField()),
                ('value_work', models.FloatField()),
            ],
        ),
    ]
