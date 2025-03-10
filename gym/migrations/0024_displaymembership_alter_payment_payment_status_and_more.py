# Generated by Django 4.2.19 on 2025-02-21 15:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gym', '0023_membership_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayMembership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', tinymce.models.HTMLField()),
            ],
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('p', 'Processing'), ('a', 'Paid'), ('e', 'Expired ')], default='p', help_text='Membership status', max_length=1, verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment', to=settings.AUTH_USER_MODEL),
        ),
    ]
