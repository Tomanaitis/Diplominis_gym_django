from django.apps import AppConfig


class GymConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym'

    def ready(self):
        from .signals import create_profile
