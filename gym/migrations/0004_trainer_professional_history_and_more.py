# Generated by Django 4.2.19 on 2025-02-19 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0003_rename_status_membership_membership_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='professional_history',
            field=models.TextField(default='Professional accomplishments...', max_length=2000, verbose_name='professional_history'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='specialization',
            field=models.CharField(default='Specialization....', max_length=100, verbose_name='Specialization'),
        ),
    ]
