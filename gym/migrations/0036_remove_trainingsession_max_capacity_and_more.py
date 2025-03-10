# Generated by Django 4.2.19 on 2025-02-22 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0035_alter_payment_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingsession',
            name='max_capacity',
        ),
        migrations.AddField(
            model_name='schedule',
            name='max_capacity',
            field=models.PositiveIntegerField(default=None, help_text='Enter max capacity', verbose_name='Capacity'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='schedule',
            name='training_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule', to='gym.trainingsession'),
        ),
    ]
