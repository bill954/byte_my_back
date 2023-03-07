from django.urls import path

from coins.views import wallets_view, coins_view, portfolio_view

urlpatterns = [
    path('wallets/', wallets_view, name='wallets'),
    path('coins/', coins_view, name='coins'),
    path('portfolio/', portfolio_view, name='portfiolio')
]
