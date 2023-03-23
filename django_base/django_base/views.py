import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from coins.models import Coin
from coins.views import get_five_days_data, get_recent_transactions, get_last_transactions

@login_required
def index(request):
    context = {
        'graph_data': json.dumps(get_five_days_data(request)),
        'coins': Coin.objects.all(),
        'recent_transactions': get_recent_transactions(request)
    }
    print('conext is here:')
    print(context)
    return render(request, 'index.html', context=context)