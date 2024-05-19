from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserSerializer

from .permissions import IsUserOwnerOrGetAndPostOnly
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsUserOwnerOrGetAndPostOnly, ] #  This line is setting the permission classes for this ViewSet. It’s using the custom permission class IsUserOwnerOrGetAndPostOnly that was imported earlier. This means that the permissions for this ViewSet will be checked according to the rules defined in IsUserOwnerOrGetAndPostOnly.
    queryset = User.objects.all()
    serializer_class = UserSerializer
    