from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    
#   *  The provided code snippet suggests the implementation of a `ready()` method within a Django application configuration class. 

# * The `ready()` method is called by Django when the application is ready to be used. In this case, the method is being used to import and activate the signals defined in the `users.signals` module.

#  * By importing the `users.signals` module within the `ready()` method, the signals defined in that module will be connected and functional when the application is ready. This allows the signals to respond to specific events or triggers within the application.
    def ready(self):
        import users.signals
