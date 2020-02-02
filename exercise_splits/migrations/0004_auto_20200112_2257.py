# Generated by Django 3.0.2 on 2020-01-13 03:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_splits', '0003_exercise_bar_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='added_note',
            field=models.TextField(default='How did you feel?'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AddField(
            model_name='exercise',
            name='sets_finished',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='repetitions',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(15)]),
        ),
    ]
