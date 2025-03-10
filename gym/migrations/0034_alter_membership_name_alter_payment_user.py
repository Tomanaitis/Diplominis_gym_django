# Generated by Django 4.2.19 on 2025-02-22 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0033_remove_membership_membership_type_membership_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='name',
            field=models.CharField(default='Trial', help_text='Trial, Basic, Flexible, Premium', max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL),
        ),
    ]
