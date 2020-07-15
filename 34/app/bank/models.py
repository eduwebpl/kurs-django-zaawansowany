from django.core.cache import cache
from django.db import models, transaction

from bank.exceptions import InsufficientFunds


class Account(models.Model):
    balance = models.IntegerField(default=0)

    @classmethod
    def withdraw(cls, acccount_id, value):
        with cache.lock(f"account_{acccount_id}"):
            account = Account.objects.get(id=acccount_id)
            if account.balance < value:
                raise InsufficientFunds()
            account.balance -= value
            account.save()
            print(f"Wypłacono {value}")

    def __str__(self):
        return f"Konto {self.id} - ${self.balance}"
