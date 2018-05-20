from django import forms

from accountingApp.models import Capital, AccountingBook, Transaction


class CapitalForm(forms.ModelForm):
    class Meta:
        model = Capital
        fields = ('amount',)


class AccountingBookForm(forms.ModelForm):
    class Meta:
        model = AccountingBook
        fields = ('name', 'balance',)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ('account', 'accounting_book', 'amount')
