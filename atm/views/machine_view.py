from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from atm.serializers.machine_serializer import Machine_Serializer


from atm.models.machine_model import Machine

from mixins .apimixin import DefaultMixin


class Machine_ViewSet(DefaultMixin, ModelViewSet):

    queryset = Machine.objects.all()
    serializer_class = Machine_Serializer
    search_fields = ('machine_id',)
    ordering = ('machine_id',)
