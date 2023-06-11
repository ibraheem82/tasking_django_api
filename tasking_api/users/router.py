# * This line imports the routers module from the rest_framework package. Routers in Django REST Framework provide a way to automatically map URL routes to corresponding viewsets.
from rest_framework import routers
# * UserViewSet is a custom viewset that defines the behavior of the views for user-related operations.
from .viewsets import UserViewSet

# * It is common to define the app_name in Django to distinguish the URLs and views of different apps when they are included in the project
app_name = "users"


# *  This line creates an instance of the DefaultRouter class from the routers module. The DefaultRouter is a built-in router class provided by Django REST Framework that automatically generates the required URL routes for the viewsets registered with it.
router = routers.DefaultRouter()

# * This line registers the UserViewSet with the router. It associates the UserViewSet with the URL path segment 'users'. This means that when a request is made to the URL path /users/, it will be routed to the appropriate viewset methods defined in UserViewSet, such as list, create, retrieve, update, and destroy.
router.register('users', UserViewSet)