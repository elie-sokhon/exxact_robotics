from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import InstallationViewSet

router = DefaultRouter()
router.register(r"installations", InstallationViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
