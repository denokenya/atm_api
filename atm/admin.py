from django.contrib import admin

from .models.machine_model import Machine
from .models.machine_refill_model import Machine_Refill
from .models.account_model import Account
from .models.atm_card_model import ATM_Card


class MachineAdmin(admin.ModelAdmin):
    list_display = [
        'machine_id',
        'location',
        'minimum_atm_balance',
        'current_balance',
        'last_refill_date',
        'next_maintenance_date',

    ]
    search_fields = ['machine_id']
    ordering = ['machine_id']
    list_display_links = ['machine_id']
    list_per_page = 15


class Machine_Refill_Admin(admin.ModelAdmin):
    list_display = [
        'refill_id',
        'machine_id',
        'refill_date',
        'previous_balance',
        'amount_refilled',


    ]
    search_fields = ['refill_id']
    ordering = ['refill_id']
    list_display_links = ['refill_id']
    list_per_page = 15


class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'acc_num',
        'name',
        'phone_num',
        'balance',

    ]
    search_fields = ['acc_num']
    ordering = ['acc_num']
    list_display_links = ['acc_num']
    list_per_page = 15


class Atm_Card_Admin(admin.ModelAdmin):
    list_display = [
        'atm_card_num',
        'account_num',
        'name',
        'date_of_issue',
        'expiry_date',

    ]
    search_fields = ['atm_card_num']
    ordering = ['atm_card_num']
    list_display_links = ['atm_card_num']
    list_per_page = 15


admin.site.register(Machine, MachineAdmin)
admin.site.register(Machine_Refill, Machine_Refill_Admin)
admin.site.register(Account, AccountAdmin)
admin.site.register(ATM_Card, Atm_Card_Admin)
