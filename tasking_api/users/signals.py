from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Profile
# It defines a receiver function create_user_profile that is triggered after a User model instance is saved.
# * This code sets up a signal receiver to automatically create a Profile instance whenever a new User instance is created, ensuring that a profile is associated with each user.
@receiver(post_save, sender=User)
# The receiver function checks if a new User instance was created and if so, it creates a corresponding Profile instance with the user field set to the created User instance.
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)