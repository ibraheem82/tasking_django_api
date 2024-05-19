from django.contrib.auth.models import User

from rest_framework import serializers
class UserSerializer(serializers.ModelSerializer):
    password 
    class Meta:
        Model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'email' 'password']
