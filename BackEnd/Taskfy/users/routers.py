from rest_framework import routers #type: ignore

from .views import UserViewSet

app_name = 'users'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
