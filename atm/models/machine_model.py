from django.db import models
from datetime import datetime
from decimal import Decimal


class Machine(models.Model):
    """Machine model stores the information of ATM_Machine
    It has 6 fields
    machine_id----->PK
    location ---> Char(200)
    minimum_atm_balance ---> Decimal
    current_balance ----> Decimal
    last_refill_date ----> DateTimeField
    next_maintainence_date ----> DateTimeField
    """
    machine_id = models.CharField(
        "Machine ID", max_length=6, unique=True, primary_key=True, null=False, blank=False)
    location = models.CharField(
        "Location", max_length=200, null=False, blank=False)
    minimum_atm_balance = models.DecimalField(
        "Minimum ATM Balance", decimal_places=2, max_digits=10)
    current_balance = models.DecimalField(
        "Current Balance", decimal_places=2, max_digits=10)
    last_refill_date = models.DateTimeField("Last Refill Date")
    next_maintenance_date = models.DateTimeField("Next maintenance Date")

    def __str__(self):
        """
        This method using Python String's method format() will
        convert machine_id and locatiom fields into  strings

        """
        return "{} {}".format(self.machine_id, self.location)

    class Meta:
        db_table = "machine"
        ordering = ["machine_id"]
        verbose_name = "machine"
        verbose_name_plural = "machines"
