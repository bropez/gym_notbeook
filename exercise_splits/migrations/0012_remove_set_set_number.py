# Generated by Django 3.0.2 on 2020-01-16 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_splits', '0011_auto_20200116_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='set',
            name='set_number',
        ),
    ]
