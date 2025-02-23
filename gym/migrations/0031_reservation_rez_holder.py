# Generated by Django 4.2.19 on 2025-02-22 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0030_membership_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='rez_holder',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
