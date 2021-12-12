from django.db import models
from datetime import datetime
from decimal import Decimal

from .transaction_model import Transaction


class Service(Transaction):
    amount = models.DecimalField(
        "AMOUNT PAID", decimal_places=2, max_digits=10)
    service = models.CharField("SERVICE DETAILS", max_length=100)

    def __str__(self):
        return self.tid

    class Meta:
        db_table = "services"
        ordering = ["tid"]
        verbose_name = "service"
        verbose_name_plural = "services"
