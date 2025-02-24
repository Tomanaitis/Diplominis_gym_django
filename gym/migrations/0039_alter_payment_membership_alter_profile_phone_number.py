# Generated by Django 4.2.19 on 2025-02-23 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0038_rename_rez_holder_reservation_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='membership',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to='gym.membership'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Enter your phone number for news letters and notifications', max_length=20, null=True, verbose_name='Phone Number'),
        ),
    ]
