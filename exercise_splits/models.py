import datetime

from django.db import models
from django.db.models import Count
from django.core.validators import MinValueValidator, MaxValueValidator

from django.urls import reverse


class WorkoutDay(models.Model):
    workout_day_choices = [
        ('Chest', 'Chest Day'),
        ('Legs', 'Leg Day'),
        ('Shoulders', 'Shoulder Day'),
        ('Back', 'Back Day'),
    ]
    workout_day = models.CharField(
        max_length=10,
        choices=workout_day_choices,
        default='Chest'
    )
    date = models.DateTimeField('workout date')
    preworkout_scoops = models.IntegerField()

    def __str__(self):
        day_title = self.workout_day + ", " + str(self.date.date())
        return day_title


class Exercise(models.Model):
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE)
    exercise_name = models.CharField(max_length=200)
    bar_type_choices = [
        ('bb', 'Barbel'),
        ('db', 'Dumbell'),
        ('bw', 'Bodyweight'),
        ('m', 'Machine'),
    ]
    bar_type = models.CharField(
        max_length=2,
        choices=bar_type_choices,
        default='bb'
    )

    # added_note = models.TextField(default="How did you feel?")

    def __str__(self):
        return self.exercise_name


class Set(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight_in_lbs = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(1000)])
    time_in_seconds = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(300)])
    repetitions = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(15)])

    def __str__(self):
        set_title = str(self.weight_in_lbs) + "lbs for " + str(self.repetitions) + " reps"
        return set_title
