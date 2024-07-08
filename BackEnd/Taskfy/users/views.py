from django.contrib.auth.models import User

from rest_framework import viewsets #type: ignore

from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing User instances.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

