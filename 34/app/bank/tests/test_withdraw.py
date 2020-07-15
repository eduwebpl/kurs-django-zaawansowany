from unittest import TestCase

from bank.exceptions import InsufficientFunds
from bank.models import Account


class TestWithdraw(TestCase):
    def test_withdraw_if_sufficient_funds(self):
        account = Account.objects.create(balance=1)
        account.withdraw(1)
        account.refresh_from_db()
        assert account.balance == 0

    def test_withdraw_if_insufficient_funds(self):
        account = Account.objects.create(balance=1)
        self.assertRaises(InsufficientFunds, account.withdraw, 2)
        account.refresh_from_db()
        assert account.balance == 1
