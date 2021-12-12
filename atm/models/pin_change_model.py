from django.db import models
from datetime import datetime
from decimal import Decimal

from .transaction_model import Transaction


class Pin_Change(Transaction):
    prev_pin = models.IntegerField("PREVIOUS PIN")
    new_pin = models.IntegerField("NEW PIN")

    def __str__(self):
        return self.tid

    class Meta:
        db_table = "pinChange"
        ordering = ["tid"]
        verbose_name = "pin change"
        verbose_name_plural = "pin changes"
