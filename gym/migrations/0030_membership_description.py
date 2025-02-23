# Generated by Django 4.2.19 on 2025-02-22 08:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0029_remove_membership_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='description',
            field=tinymce.models.HTMLField(blank=True, default=None),
        ),
    ]
