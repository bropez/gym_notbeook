# Generated by Django 3.0.2 on 2020-01-16 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_splits', '0010_auto_20200114_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='current_set',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='top_weight',
        ),
    ]