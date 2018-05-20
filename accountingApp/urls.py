from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('capitals', views.capital, name='capital'),
    path('accounting_books', views.accounting_book, name='accounting_book'),
    path('accounting_book_transactions/<int:accounting_book_id>', views.accounting_book_transaction,
         name='accounting_book_transaction'),
]
#
# app_name = 'accountingApp'
# urlpatterns = [
#     path('', views.IndexView.as_view(), name='index'),
#     path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#     path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
