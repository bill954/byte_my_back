from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from coins.utils import generate_transactions, generate_currencies
from coins.models import Coin, Transaction


from datetime import timedelta
import random

@login_required
def wallets_view(request):
    return render(request, 'coins/wallets.html')

@login_required
def coins_view(request):
    return render(request, 'coins/coins.html')

@login_required
def portfolio_view(request):
    coins = Coin.objects.all()
    for coin in coins:
        coin.user_data = 4
        # falta conectar los datos de cada currency con el usuario
    context = {
        'coins': coins
    }
    return render(request, 'coins/portfolio.html', context=context)

def generate_data(request):
    print(generate_transactions())
    return HttpResponse('Data generated')

def create_currencies(request):
    generate_currencies()
    return HttpResponse('Currencies generated')

def get_five_days_data(request):
    context = {
        'data':[]
    }

    date_array = [Transaction.get_last_day()]

    for i in range(1, 5):
        date_array.append((date_array[0] - timedelta(days=i)).strftime('%d/%m'))

    date_array[0] = date_array[0].strftime('%d/%m')
            
    context['dates'] = date_array[::-1]
    for coin in Coin.objects.all():
        context['data'].append(
            {
            'name':coin.name,
            'data':coin.get_last_five_days_data()
            }
        )
    return context

def get_recent_transactions(request):
    since_day = Transaction.get_last_day() - timedelta(days=120)
    transactions = random.choices(Transaction.objects.filter(date__gte=since_day), k=6)
    return transactions

def get_last_transactions(request):
    last_transactions = []
    for coin in Coin.objects.all():
        last_transactions.append(Transaction.objects.filter(coin=coin).order_by('-date')[0:8])
    return last_transactions