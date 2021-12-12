from django.db import models
from datetime import datetime
from decimal import Decimal

from .transaction_model import Transaction


class Balance_Enquiry(Transaction):
    bal_amount = models.DecimalField(
        "BALANCE AMOUNT", decimal_places=2, max_digits=10)

    def __str__(self):
        return self.tid

    class Meta:
        db_table = "balanceEnquiry"
        ordering = ["tid"]
        verbose_name = "balance enquiry"
        verbose_name_plural = "balance enquiries"
