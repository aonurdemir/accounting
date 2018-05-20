# Create your tests here.
from django.contrib.auth.models import User
from django.test import TestCase

from accountingApp.models import AccountingBook, Capital


class AccountingBookTests(TestCase):
    def test_add_amount_to_accounting_book_balance(self):
        ab = AccountingBook(user=User(), name="book", capital=Capital(), balance=0)
        ab.add_amount(1000)
        self.assertEqual(ab.balance, 1000)

    def test_sub_amount_to_accounting_book_balance(self):
        ab = AccountingBook(user=User(), name="book", capital=Capital(), balance=0)
        ab.sub_amount(1000)
        self.assertEqual(ab.balance, -1000)
