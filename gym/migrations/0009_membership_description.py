# Generated by Django 4.2.19 on 2025-02-20 14:58

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0008_remove_client_email_remove_client_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='description',
            field=tinymce.models.HTMLField(default=None),
            preserve_default=False,
        ),
    ]
