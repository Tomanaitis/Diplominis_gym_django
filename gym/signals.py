from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Automatically creates a Profile instance when a new User is created.
    """
    if created:
        Profile.objects.create(user=instance)

