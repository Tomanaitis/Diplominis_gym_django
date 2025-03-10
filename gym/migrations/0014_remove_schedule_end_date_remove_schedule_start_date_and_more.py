# Generated by Django 4.2.19 on 2025-02-21 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0013_remove_trainingsession_schedule_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='start_date',
        ),
        migrations.RemoveField(
            model_name='trainingsession',
            name='location',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(default=datetime.date.today, help_text='Enter date', verbose_name='date'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='location',
            field=models.CharField(blank=True, choices=[('1', 'Main Studio'), ('2', 'Yoga Room'), ('3', 'Cardio Zone'), ('4', 'Outdoor Terrace'), ('5', 'Functional Training Area')], default='1', help_text='Gym class locations', max_length=1, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='trainingsession',
            name='duration',
            field=models.DurationField(default='01:00:00', help_text='Default time is 1 hour'),
        ),
    ]
