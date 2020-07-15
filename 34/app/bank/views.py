from django.http import HttpResponse
from django.views import View

from bank.exceptions import InsufficientFunds
from bank.models import Account


class WithdrawView(View):
    def post(self, request, *args, **kwargs):
        try:
            value = int(request.POST['value'])
            account = Account.objects.get()
            account.withdraw(value)
            return HttpResponse(account.balance)
        except ValueError:
            return HttpResponse("Niepoprawny parametr value", status=400)
        except InsufficientFunds:
            return HttpResponse("Brak środków na koncie", status=400)
