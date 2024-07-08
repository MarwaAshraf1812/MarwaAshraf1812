from django.contrib.auth.models import User

from rest_framework import serializers #type: ignore


class UserSerializer(serializers.ModelSerializer):
    """
    A serializer class for the User model.
    
    """
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'first_name', 'last_name', 'profile']