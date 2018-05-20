from django.contrib import admin

# Register your models here.
from accountingApp.models import Capital, AccountingBook, Account, Transaction

admin.site.register(Capital)
admin.site.register(AccountingBook)
admin.site.register(Account)
admin.site.register(Transaction)
