from django.contrib import admin
from coins.models import Card, Coin, Transaction, CoinCurrency

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('card_name',)
    
@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('coin', 'transaction_type', 'date')
    
@admin.register(CoinCurrency)
class CoinCurrencyAdmin(admin.ModelAdmin):
    list_display = ('user', 'coin', 'amount')