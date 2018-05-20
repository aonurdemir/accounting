from django import forms

from accountingApp.models import Capital


class CapitalForm(forms.ModelForm):
    class Meta:
        model = Capital
        fields = ('amount',)
