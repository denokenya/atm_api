from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from atm.serializers.atm_card_serializer import ATM_Card_Serializer


from atm.models.atm_card_model import ATM_Card

from mixins .apimixin import DefaultMixin


class ATM_Card_ViewSet(DefaultMixin, ModelViewSet):

    queryset = ATM_Card.objects.all()
    serializer_class = ATM_Card_Serializer
    search_fields = ('acc_num',)
    ordering = ('acc_num',)
