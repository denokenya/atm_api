from django.contrib import admin

from .models.machine_model import Machine
from .models.machine_refill_model import Machine_Refill
from .models.account_model import Account
from .models.atm_card_model import ATM_Card
from .models.balance_enquiry_model import Balance_Enquiry
from .models.phone_change_model import Phone_Change
from .models.pin_change_model import Pin_Change
from .models.cash_transfer_model import Cash_Transfer
from .models.cash_withdrawal_model import Cash_Withdrawal
from .models.services_model import Service


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


class Balance_Enquiry_Admin(admin.ModelAdmin):
    list_display = [
        'tid',
        'machine_id',
        'date_time',
        'status',
        'rescode',
        'type_trans',
        'bal_amount',
    ]
    search_fields = ['tid']
    ordering = ['tid']
    list_display_links = ['tid']
    list_per_page = 15


class Phone_Change_Admin(admin.ModelAdmin):
    list_display = [
        'tid',
        'date_time',
    ]
    search_fields = ['tid']
    ordering = ['tid']
    list_display_links = ['tid']
    list_per_page = 15


class Pin_Change_Admin(admin.ModelAdmin):
    list_display = [
        'tid',
        'date_time',
    ]
    search_fields = ['tid']
    ordering = ['tid']
    list_display_links = ['tid']
    list_per_page = 15


class Cash_Transfer_Admin(admin.ModelAdmin):
    list_display = [
        'tid',
        'date_time',
    ]
    search_fields = ['tid']
    ordering = ['tid']
    list_display_links = ['tid']
    list_per_page = 15


class Cash_Withdrawal_Admin(admin.ModelAdmin):
    list_display = [
        'tid',
        'date_time',
    ]
    search_fields = ['tid']
    ordering = ['tid']
    list_display_links = ['tid']
    list_per_page = 15


class Service_Admin(admin.ModelAdmin):
    list_display = [
        'tid',
        'date_time',
    ]
    search_fields = ['tid']
    ordering = ['tid']
    list_display_links = ['tid']
    list_per_page = 15


admin.site.register(Machine, MachineAdmin)
admin.site.register(Machine_Refill, Machine_Refill_Admin)
admin.site.register(Account, AccountAdmin)
admin.site.register(ATM_Card, Atm_Card_Admin)
admin.site.register(Balance_Enquiry, Balance_Enquiry_Admin)
admin.site.register(Phone_Change, Phone_Change_Admin)
admin.site.register(Pin_Change, Pin_Change_Admin)
admin.site.register(Cash_Transfer, Cash_Transfer_Admin)
admin.site.register(Cash_Withdrawal, Cash_Withdrawal_Admin)
admin.site.register(Service, Service_Admin)
