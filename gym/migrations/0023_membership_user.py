# Generated by Django 4.2.19 on 2025-02-21 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0022_alter_payment_payment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='membership', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
