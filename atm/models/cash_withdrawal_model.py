from django.db import models
from datetime import datetime
from decimal import Decimal

from .transaction_model import Transaction


class Cash_Withdrawal(Transaction):
    amt_with = models.DecimalField(
        "AMOUNT WITHDRAWN", decimal_places=2, max_digits=10)
    cur_bal = models.DecimalField(
        "CURRENT BALANCE", decimal_places=2, max_digits=10)

    def __str__(self):
        return self.tid

    class Meta:
        db_table = "cashWithdrawal"
        ordering = ["tid"]
        verbose_name = "cash withdrawal"
        verbose_name_plural = "cash withdrawals"
