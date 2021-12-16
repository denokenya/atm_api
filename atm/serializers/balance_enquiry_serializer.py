from django.db.models import fields
from rest_framework import serializers

from atm.models.balance_enquiry_model import Balance_Enquiry


class Balance_Enquiry_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model = Balance_Enquiry
        fields = [
            'atm_num',
            'machine_id',
            'tid',
            'date_time',
            'status',
            'rescode',
            'type_trans',
            'bal_amount',
     
        ]
        
