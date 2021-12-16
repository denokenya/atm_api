from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from atm.serializers.balance_enquiry_serializer import Balance_Enquiry_Serializer


from atm.models.balance_enquiry_model import Balance_Enquiry

from mixins .apimixin import DefaultMixin


class Balance_Enquiry_ViewSet(DefaultMixin, ModelViewSet):

    queryset = Balance_Enquiry.objects.all()
    serializer_class = Balance_Enquiry_Serializer
    search_fields = ('acc_num',)
    ordering = ('acc_num',)
