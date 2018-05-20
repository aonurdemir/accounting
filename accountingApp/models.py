from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Capital(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    amount = models.FloatField(blank=False)


class AccountingBook(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    capital = models.ForeignKey(Capital, on_delete=models.DO_NOTHING)
    balance = models.FloatField(blank=False)

    def add_amount(self, amount):
        self.balance += amount

    def sub_amount(self, amount):
        self.balance -= amount
