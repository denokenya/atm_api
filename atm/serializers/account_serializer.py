from django.db.models import fields
from rest_framework import serializers

from atm.models.account_model import Account


class Account_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = Account
        fields = [
            'acc_num',
            'name',
            'phone_num',
            'balance',
     
        ]
        
