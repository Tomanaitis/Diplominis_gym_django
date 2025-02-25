from django.apps import AppConfig


class GymConfig(AppConfig):
    """
    Configuration for the Gym application, setting up the app name and
    automatically using BigAutoField for model primary keys.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gym'

    def ready(self):
        """
        Importing signals to initialize profile creation
        """
        from .signals import create_profile

