from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    A signal receiver to create a profile for a new user.

    Args:
        sender: The model class.
        instance: The actual instance being saved.
        created: A boolean that's True if a new record was created.
    """
    if created:
        Profile.objects.create(user=instance)
        