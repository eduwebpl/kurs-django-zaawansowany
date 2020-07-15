from django.db import models

from bank.exceptions import InsufficientFunds


class Account(models.Model):
    balance = models.IntegerField(default=0)

    def withdraw(self, value):
        if self.balance < value:
            raise InsufficientFunds()
        self.balance -= value
        self.save()
        print(f"Wypłacono {value}")

    def __str__(self):
        return f"Konto {self.id} - ${self.balance}"
