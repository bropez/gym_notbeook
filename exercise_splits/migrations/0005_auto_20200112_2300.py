# Generated by Django 3.0.2 on 2020-01-13 04:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_splits', '0004_auto_20200112_2257'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercise',
            old_name='sets_finished',
            new_name='current_set',
        ),
    ]
