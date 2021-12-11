from django.db import models
from datetime import datetime
from decimal import Decimal

from .machine_model import Machine


class Machine_Refill(models.Model):

    """
    # MachineRefill model stores the information of refill for ATM machine.
    # It has 5 fields
    # refill_id -->CharField
    # machine_id ---> ForeignKey of Machine
    # refill_date ---> DateTimeField
    # previous_balance ---> DecimalField
    # amount_refilled ----> Decimal

    """
    refill_id = models.CharField(
        "Refill ID", max_length=6, unique=True, primary_key=True, null=False, blank=False)
    machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    refill_date = models.DateTimeField("Refill Date")
    previous_balance = models.DecimalField(
        "Previous Balance", decimal_places=2, max_digits=10)
    amount_refilled = models.DecimalField(
        "Amount Refilled", decimal_places=2, max_digits=10)

    def __str__(self):
        return self.refill_id

    class Meta:
        db_table = "machineRefill"
        ordering = ["refill_id"]
        verbose_name = "machine refill"
        verbose_name_plural = "machines refill"
