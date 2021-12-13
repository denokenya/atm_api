from django.db.models import fields
from rest_framework import serializers

from atm.models.machine_model import Machine


class Machine_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = Machine
        fields = [
            'machine_id',
            'location',
            'minimum_atm_balance',
            'current_balance',
            'last_refill_date',
            'next_maintenance_date',  
        ]
        
