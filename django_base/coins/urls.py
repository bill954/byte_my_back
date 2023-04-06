from django.urls import path

from coins.views import wallets_view, coins_view, portfolio_view, generate_data, get_five_days_data, create_currencies, delete_card

urlpatterns = [
    path('wallets/', wallets_view, name='wallets'),
    path('coin_details/<int:pk>', coins_view, name='coin_details'),
    path('portfolio/', portfolio_view, name='portfiolio'),
    path('generate_data', generate_data, name='generate_data'),
    path('get_five_days_data/', get_five_days_data, name='get_five_days_data'),
    path('create_currencies/', create_currencies, name='create_currencies'),
    path('card/delete/<int:card_id>', delete_card, name='delete_card')
]