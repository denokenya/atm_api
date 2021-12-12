from django.db import models
from datetime import datetime
from decimal import Decimal

from .account_model import Account


class ATM_Card(models.Model):

    """
        # ATM_Card model stores the information of ATM cards
        # It has 9 fields
        # atmcard_num ---> ForeignKey of Account
        # name ---> Char(100)
        # pin ---> Integer
        # date_of_issue ---> DateTimeField
        # expiry_date ---> DateTimeField
        # address --> Char(300)
        # two_factor ---> Boolean
        # phone_num ---> BigInteger
        # card_status ---> Boolean
    """

    atm_card_num = models.BigIntegerField("ATM Card Number", primary_key=True)
    account_num = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField("NAME ON CARD", max_length=100)
    pin = models.IntegerField("PIN")
    date_of_issue = models.DateTimeField("DATE OF ISSUE")
    expiry_date = models.DateTimeField("EXPIRY DATE")
    address = models.CharField("ADDRESS", max_length=300)
    two_factor = models.BooleanField("TWO FACTOR AUTHENTICATION STATUS")
    phone_num = models.BigIntegerField(
        "PHONE NUMBER FOR AUTHENTICATION", unique=True)
    card_status = models.BooleanField("CARD STATUS", default=False)

    def __str__(self):
        return self.atm_card_num

    class Meta:
        db_table = "atmcard"
        ordering = ["atm_card_num"]
        verbose_name = "atm card"
        verbose_name_plural = "atm cards"
