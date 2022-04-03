# Generated by Django 4.0.3 on 2022-04-03 18:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nit', models.PositiveIntegerField(unique=True,
                                                    validators=[django.core.validators.MinLengthValidator(6),
                                                                django.core.validators.MaxLengthValidator(10)])),
                ('name', models.TextField(max_length=40, validators=[django.core.validators.MinLengthValidator(3)])),
                ('work_hour', models.PositiveIntegerField()),
                ('value_work', models.FloatField()),
            ],
        ),
    ]
