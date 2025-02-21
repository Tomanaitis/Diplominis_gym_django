# Generated by Django 4.2.19 on 2025-02-21 16:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0026_alter_displaymembership_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainingSessionReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(max_length=2000, verbose_name='Review')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('training_session', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='gym.trainingsession')),
            ],
        ),
    ]
