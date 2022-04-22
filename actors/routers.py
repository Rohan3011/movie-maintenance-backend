from rest_framework import routers

from .views import ActorViewSet

router = routers.DefaultRouter()
router.register('actors', ActorViewSet)
