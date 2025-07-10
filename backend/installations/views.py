from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from .models import Installation
from .serializers import InstallationSerializer


class InstallationViewSet(viewsets.ModelViewSet):
    queryset = Installation.objects.all().order_by("gid")
    serializer_class = InstallationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["codepostal", "statutseveso", "etatactivite"]
