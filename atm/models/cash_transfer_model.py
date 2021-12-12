from django.db import models
from datetime import datetime
from decimal import Decimal

from .transaction_model import Transaction


class Cash_Transfer(Transaction):
    ben_acc_num = models.BigIntegerField("BENEFICIARY ACCOUNT NUMBER")
    ben_name = models.CharField("BENEFICIARY NAME", max_length=100)
    amt_trans = models.DecimalField("AMOUNT", decimal_places=2, max_digits=10)

    def __str__(self):
        return self.tid

    class Meta:
        db_table = "cashTransfer"
        ordering = ["tid"]
        verbose_name = "cash transfer"
        verbose_name_plural = "cash transfers"
