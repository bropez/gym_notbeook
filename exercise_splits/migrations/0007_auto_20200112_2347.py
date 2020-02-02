# Generated by Django 3.0.2 on 2020-01-13 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_splits', '0006_auto_20200112_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='bar_type',
            field=models.CharField(choices=[('bb', 'Barbel'), ('db', 'Dumbell'), ('bw', 'Bodyweight')], default='bb', max_length=2),
        ),
    ]
