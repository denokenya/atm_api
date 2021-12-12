from django.db import models
from datetime import datetime
from decimal import Decimal

from .transaction_model import Transaction


class Phone_Change(Transaction):
    prev_phone = models.BigIntegerField("PREVIOUS PHONE NO")
    new_phone = models.BigIntegerField("NEW PHONE NO")

    def __str__(self):
        return self.tid

    class Meta:
        db_table = "phoneChange"
        ordering = ["tid"]
        verbose_name = "phone change"
        verbose_name_plural = "phone changes"
