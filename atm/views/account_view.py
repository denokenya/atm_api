from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from atm.serializers.account_serializer import Account_Serializer


from atm.models.account_model import Account

from mixins .apimixin import DefaultMixin


class Machine_Refill_ViewSet(DefaultMixin, ModelViewSet):

    queryset = Account.objects.all()
    serializer_class = Account_Serializer
    search_fields = ('acc_num',)
    ordering = ('acc_num',)
