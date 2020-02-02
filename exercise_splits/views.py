from django.shortcuts import render
from django.views import generic

from django import forms

from django.urls import reverse, reverse_lazy

from django.shortcuts import get_object_or_404

from .models import WorkoutDay, Exercise, Set
from .forms import WorkoutDayCreateForm, ExerciseCreateForm, SetCreateForm


class WD_CreateView(generic.CreateView):
    template_name = 'exercise_splits/wd_create.html'
    form_class = WorkoutDayCreateForm

    def get_success_url(self):
        return reverse('workouts:index')


class WD_UpdateView(generic.UpdateView):
    # TODO: Change this to an updateview template and not use create
    template_name = 'exercise_splits/wd_create.html'
    form_class = WorkoutDayCreateForm

    def get_success_url(self):
        return reverse('workouts:index')

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(WorkoutDay, pk=pk_)


class WD_DeleteView(generic.DeleteView):
    template_name = 'exercise_splits/wd_delete.html'

    def get_success_url(self):
        return reverse('workouts:index')

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(WorkoutDay, pk=pk_)


class WD_ListView(generic.ListView):
    template_name = 'exercise_splits/index.html'
    context_object_name = 'workout_list'

    def get_queryset(self):
        # TODO: make this the past week's workouts
        """
        Returns this past week's workouts
        """
        return WorkoutDay.objects.all()


class WD_DetailView(generic.DetailView):
    model = WorkoutDay
    template_name = 'exercise_splits/wd_detail.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(WorkoutDay, pk=pk_)    


class E_CreateView(generic.CreateView):
    model = Exercise
    template_name = 'exercise_splits/e_create.html'
    form_class = ExerciseCreateForm

    def get_success_url(self):
        return reverse('workouts:wd_detail', kwargs={'pk': self.object.workout_day.pk })

    def form_valid(self, form):
        form.instance.workout_day_id = self.kwargs.get('wd_id')
        return super(E_CreateView, self).form_valid(form)


class E_UpdateView(generic.UpdateView):
    # TODO: Change this to an updateview template and not use create
    template_name = 'exercise_splits/e_create.html'
    form_class = ExerciseCreateForm

    def get_success_url(self):
        return reverse('workouts:wd_detail', kwargs={'pk': self.object.workout_day.pk })

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Exercise, pk=pk_)


class E_DeleteView(generic.DeleteView):
    template_name = 'exercise_splits/e_delete.html'

    def get_success_url(self):
        return reverse_lazy('workouts:wd_detail', kwargs={'pk': self.object.workout_day.pk })

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Exercise, pk=pk_)


class E_DetailView(generic.DetailView):
    model = Exercise
    template_name = 'exercise_splits/e_detail.html'
    context_object_name = 'ex'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Exercise, pk=pk_)


class S_CreateView(generic.CreateView):
    model = Set
    template_name = 'exercise_splits/s_create.html'
    form_class = SetCreateForm

    def get_success_url(self):
        return reverse('workouts:e_detail', kwargs={'pk': self.object.exercise.pk})

    def form_valid(self, form):
        form.instance.exercise_id = self.kwargs.get('ex_id')
        return super(S_CreateView, self).form_valid(form)


class S_UpdateView(generic.UpdateView):
    # TODO: Change this to an updateview template and not use create
    template_name = 'exercise_splits/s_create.html'
    form_class = SetCreateForm

    def get_success_url(self):
        return reverse('workouts:e_detail', kwargs={'pk': self.object.exercise.pk})

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Set, pk=pk_)


class S_DeleteView(generic.DeleteView):
    template_name = 'exercise_splits/s_delete.html'

    def get_success_url(self):
        return reverse_lazy('workouts:e_detail', kwargs={'pk': self.object.exercise.pk })

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Set, pk=pk_)


class S_DetailView(generic.DetailView):
    model = Set
    template_name = 'exercise_splits/s_detail.html'
    context_object_name = 'set'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Set, pk=pk_)
