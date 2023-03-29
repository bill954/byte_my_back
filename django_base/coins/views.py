import random

from datetime import timedelta, datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from coins.utils import generate_transactions, generate_currencies
from coins.models import Coin, Transaction, Card, CoinCurrency
from coins.forms import CardForm


@login_required
def wallets_view(request):
    if request.method == 'GET':
        context = {
            'cards': Card.objects.filter(user=request.user)
        }
        return render(request, 'coins/wallets.html', context)

    elif request.method == 'POST':
        # request.POST is inmutable, so we need to make a copy to change the valid_date format
        data = request.POST.copy()
        data['valid_date'] = datetime.strptime(request.POST['valid_date'], '%m/%y').date()
        form = CardForm(data)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.balance = random.randint(10000, 30000) * random.random()
            card.save()
            return redirect('wallets')
        else:
            context = {
            'cards': Card.objects.filter(user=request.user),
            'errors': form.errors
        }
            return render(request, 'coins/wallets.html', context=context)

    return redirect('index')

@login_required
def delete_card(request, card_id):
    Card.objects.get(id=card_id).delete()
    return redirect('wallets')

@login_required
def coins_view(request):
    return render(request, 'coins/coins.html')

@login_required
def portfolio_view(request):
    coins = Coin.objects.all()
#    currencies = CoinCurrency.objects.all()
    for coin in coins:
        amount = coin.currency.filter(user=request.user).first().amount
        price = coin.get_last_day_price()
        coin.user_currency = amount * price
        # other solution
        # for currency in currencies:
        #     if currency.user == request.user and currency.coin == coin:
        #         price = coin.get_last_day_price()
        #         coin.amount = currency.amount * price

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