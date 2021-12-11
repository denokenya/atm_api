from django.db import models
from datetime import datetime
from decimal import Decimal


class Account(models.Model):
    """
    # Account_Ext model stores the information of account.
    # I t has 5 fields
    ## acc_num = BigInteger
    # atmcard_num ---> BigInteger
    # name --> Char
    # phone_num --> BigInteger
    # balance --> Decimal

    """

    acc_num = models.BigIntegerField("Account Number", primary_key=True)
    name = models.CharField("NAME", max_length=100)
    phone_num = models.BigIntegerField("Phone NUMBER")
    balance = models.DecimalField("Balance", decimal_places=2, max_digits=10)

    def __str__(self):
        return self.acc_num

    class Meta:
        db_table = "account"
        ordering = ["acc_num"]
        verbose_name = "account"
        verbose_name_plural = "accounts"
