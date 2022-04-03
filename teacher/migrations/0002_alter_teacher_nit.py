# Generated by Django 4.0.3 on 2022-04-03 21:54

from django.db import migrations, models
import teacher.models


class Migration(migrations.Migration):
    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='nit',
            field=models.PositiveIntegerField(unique=True, validators=[teacher.models.validator_nit]),
        ),
    ]
