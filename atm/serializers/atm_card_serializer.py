from django.db.models import fields
from rest_framework import serializers

from atm.models.atm_card_model import ATM_Card


class ATM_Card_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = ATM_Card
        fields = [
            'atm_card_num',
            'account_num',
            'name',
            'pin',
            'date_of_issue',
            'expiry_date',
            'address',
            'two_factor',
            'phone_num',
            'card_status',
     
        ]
        
