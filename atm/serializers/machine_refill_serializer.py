from django.db.models import fields
from rest_framework import serializers

from atm.models.machine_refill_model import Machine_Refill


class Machine_Refill_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = Machine_Refill
        fields = [
            'refill_id',
            'machine_id',
            'refill_date',
            'previous_balance',
            'amount_refilled',
             
        ]
        
