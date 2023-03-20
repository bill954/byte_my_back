from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from coins.utils import generate_transactions
from coins.models import Coin, Transaction

from datetime import timedelta

@login_required
def wallets_view(request):
    return render(request, 'coins/wallets.html')

@login_required
def coins_view(request):
    return render(request, 'coins/coins.html')

@login_required
def portfolio_view(request):
    return render(request, 'coins/portfolio.html')

def generate_data(request):
    print(generate_transactions())
    return HttpResponse('Data generated')

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
    print(context)
    return context