from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Profile

# * anytime user a is created a corresponding profile should be created from them.
# It defines a receiver function create_user_profile that is triggered after a User model instance is saved.
# * This code sets up a signal receiver to automatically create a Profile instance whenever a new User instance is created, ensuring that a profile is associated with each user.
@receiver(post_save, sender=User)
# The receiver function checks if a new User instance was created and if so, it creates a corresponding Profile instance with the user field set to the created User instance.
def create_user_profile(sender, instance, created, **kwargs):
  if created:
    Profile.objects.create(user=instance)
    
    
    # * automatically sets a username for a User instance before it's saved to the database. 
    '''
    @receiver: This is a decorator that registers the function to receive signals. In this case, it's listening for the pre_save signal, which is sent before an object is saved to the database.
sender=User: This specifies that the signal is only sent when a User object is being saved.
set_username: This is the function that will be called when the signal is received.

  **Arguments:**
  sender: The class of the object being saved (in this case, User).
  instance: The actual object being saved (an instance of User).
    '''
@receiver(pre_save, sender=User)
def set_username(sender, instance, **kwargs):
  
  #   If the username attribute of the User instance is empty (not instance.username), the function generates a username based on the first_name and last_name attributes.
    # 
   
    if not instance.username:
      username = f'{instance.first_name}_{instance.last_name}'.lower()
      counter = 1
      while User.objects.filter(username=username):
        #  It uses a counter to ensure the generated username is unique by appending a number to the end (e.g., john_doe, john_doe_1, john_doe_2, etc.).
        username = f'{instance.first_name}_{instance.last_name}_{counter}'.lower()
        counter += 1
         #  ! Finally, it sets the username attribute of the User instance to the generated username.
      instance.username = username
      