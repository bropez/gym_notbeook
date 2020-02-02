from django import forms

from .models import WorkoutDay, Exercise, Set


class WorkoutDayCreateForm(forms.ModelForm):
    class Meta:
        model = WorkoutDay
        fields = ['workout_day', 'date', 'preworkout_scoops']
        widgets = {
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control datetimepicker-input',
                'data-target': '#datetimepicker1'
            })
        }

   
class ExerciseCreateForm(forms.ModelForm):
    class Meta:
        model = Exercise
        # fields = ['exercise_name', 'bar_type', 'top_weight', 'current_set', 'added_note']
        # fields = ['exercise_name', 'bar_type', 'added_note']
        fields = ['exercise_name', 'bar_type']


class SetCreateForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = ['weight_in_lbs', 'repetitions']
