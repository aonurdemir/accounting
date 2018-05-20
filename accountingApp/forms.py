from django import forms

from accountingApp.models import Capital, AccountingBook


class CapitalForm(forms.ModelForm):
    class Meta:
        model = Capital
        fields = ('amount',)


class AccountingBookForm(forms.ModelForm):
    class Meta:
        model = AccountingBook
        fields = ('name', 'balance',)
