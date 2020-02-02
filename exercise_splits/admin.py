from django.contrib import admin

from .models import WorkoutDay, Exercise, Set


class SetInline(admin.TabularInline):
    model = Set
    extra = 1

class ExerciseInline(admin.TabularInline):
    model = Exercise
    exclude = ['added_note', 'current_set']
    extra = 1


class WorkoutDayAdmin(admin.ModelAdmin):
    inlines = [ExerciseInline]


class ExerciseAdmin(admin.ModelAdmin):
    inlines = [SetInline]


admin.site.register(WorkoutDay, WorkoutDayAdmin)
admin.site.register(Exercise, ExerciseAdmin)