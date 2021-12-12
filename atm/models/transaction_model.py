from django.db import models
from datetime import datetime
from decimal import Decimal
from .atm_card_model import ATM_Card
from .machine_model import Machine


class Transaction(models.Model):

    """
    # Transaction is the abstract class which has sub-classes
    # It has 7 fields
    # atmcard_num ---> ForeignKey of Account_Ext
    # machine_id ---> ForeignKey of Machine
    # tid ---> Integer
    # date_time ---> DateTimeField
    # status ---> Char(100)
    # rescode ---> Integer
    # type_trans ---> Char(100)
    """
    atmcard_num = models.ForeignKey(ATM_Card)
    machine_id = models.ForeignKey(Machine)
    tid = models.IntegerField("TRANSACTION ID", primary_key=True)
    date_time = models.DateTimeField("DATE TIME OF TRANSACTION")
    status = models.CharField("STATUS", max_length=100)
    rescode = models.IntegerField("RESPONSE CODE")
    type_trans = models.CharField("TRANSACTION TYPE", max_length=100)

    class Meta:
        abstract = True
