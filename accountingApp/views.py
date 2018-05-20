from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.utils.translation import gettext_lazy as _

# Create your views here.
from accountingApp.forms import CapitalForm, AccountingBookForm


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
