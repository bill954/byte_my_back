from django.shortcuts import render, redirect

def wallets_view(request):
    return render(request, 'coins/wallets.html')

def coins_view(request):
    return render(request, 'coins/coins.html')

def portfolio_view(request):
    return render(request, 'coins/portfolio.html')