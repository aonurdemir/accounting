from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

# Create your views here.
from accountingApp.forms import CapitalForm, AccountingBookForm, TransactionForm
from accountingApp.models import Account, AccountingBook


@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user, })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def capital(request):
    if request.method == 'POST':
        form = CapitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        if request.user.capital:
            return render(request, 'capital.html', {'msg': _("You have already a capital")})
        else:
            return render(request, 'capital.html', {'form': CapitalForm()})


@login_required
def accounting_book(request):
    if request.method == 'POST':
        form = AccountingBookForm(request.POST)
        if form.is_valid():
            accountingBook = form.instance
            accountingBook.capital = request.user.capital
            form.save()
            accountingBook.user.set([request.user])
            form.save()
            return redirect('home')
    else:
        payload = {'form': AccountingBookForm(), }
        if request.user.accountingbook_set.count() > 0:
            payload['accountingBooks'] = request.user.accountingbook_set.all()

        return render(
            request,
            'accounting_book.html', payload
        )


def accounting_book_transaction(request, accounting_book_id):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction')
    else:
        form = TransactionForm()
        form.fields["accounting_book"].queryset = AccountingBook.objects.filter(id=accounting_book_id)
        form.fields["accounting_book"].initial = AccountingBook.objects.get(pk=accounting_book_id).id
        form.fields["accounting_book"].empty_label = None
        payload = {'form': form, }
        if AccountingBook.objects.get(pk=accounting_book_id).transaction_set.count() > 0:
            payload['transactions'] = AccountingBook.objects.get(pk=accounting_book_id).transaction_set.all()

        return render(
            request,
            'transaction.html', payload
        )
