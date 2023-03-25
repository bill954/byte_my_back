from django.urls import path

from coins.views import wallets_view, coins_view, portfolio_view, generate_data, get_five_days_data, create_currencies

urlpatterns = [
    path('wallets/', wallets_view, name='wallets'),
    path('coins/', coins_view, name='coins'),
    path('portfolio/', portfolio_view, name='portfiolio'),
    path('generate_data', generate_data, name='generate_data'),
    path('get_five_days_data', get_five_days_data, name='get_five_days_data'),
    path('create_currencies', create_currencies, name='create_currencies')
]