# Generated by Django 4.2.19 on 2025-02-22 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0032_remove_membership_profile_remove_payment_profile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='membership_type',
        ),
        migrations.AddField(
            model_name='membership',
            name='name',
            field=models.CharField(default=None, max_length=50, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
