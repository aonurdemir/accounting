from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Capital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField(blank=False)

    def __str__(self):
        return "{0} - {1}".format(self.user.username, self.amount)


class Account(models.Model):
    types = [
        ("credit_card", "Credit Card"),
        ("bank_account", "Bank Account"),
        ("cash", "Cash")
    ]
    name = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=20, choices=[(key, value) for (key, value) in types])
    balance = models.FloatField(blank=False)

    def __str__(self):
        return self.name if self.name is not None else "no name"


class AccountingBook(models.Model):
    name = models.CharField(max_length=255)
    user = models.ManyToManyField(User, through='AccountingBookUser', through_fields=('accounting_book', 'user',), )
    capital = models.ForeignKey(Capital, on_delete=models.DO_NOTHING)
    balance = models.FloatField(blank=False, default=0.0)
    accounts = models.ManyToManyField(Account, through='AccountingBookAccount',
                                      through_fields=('accounting_book', 'account',), )

    def __str__(self):
        return self.name

    def add_amount(self, amount):
        self.balance += amount

    def sub_amount(self, amount):
        self.balance -= amount


class AccountingBookUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accounting_book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE)


class AccountingBookAccount(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    accounting_book = models.ForeignKey(AccountingBook, on_delete=models.CASCADE)


class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    accounting_book = models.ForeignKey(AccountingBook, null=True, on_delete=models.DO_NOTHING)
    amount = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} / {1} / Account Balance: {2}".format(self.account.name, self.amount, self.account.balance)


class Installment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    accounting_book = models.ForeignKey(AccountingBook, null=True, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=255)
    amount = models.FloatField(blank=False)
    count = models.IntegerField(blank=False)
