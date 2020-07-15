from django.contrib import admin

from bank.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass
