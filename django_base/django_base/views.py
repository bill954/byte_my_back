import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from coins.models import Coin
from coins.views import get_five_days_data

@login_required
def index(request):
    context = {
        'graph_data': json.dumps(get_five_days_data()),
        'coins': Coin.objects.all(),
    }    
    return render(request, 'index.html', context=context)