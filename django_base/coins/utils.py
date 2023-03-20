import random
from django.utils import timezone
from datetime import timedelta

from coins.models import Transaction, Coin

def generate_price():
    return random.randint(10000, 30000) * random.random()

def generate_amount():
    return random.randint(1, 20) * random.random()

def generate_transaction_type():
    return random.choice(['buy', 'sell'])

def generate_transactions():
    
    today = timezone.now().date()
    
    transactions_to_create = []
    
    for coin in Coin.objects.all():
        for i in range(1, 31):
            for j in range(1, 31):
                transactions_to_create.append(
                    Transaction(
                        coin = coin,
                        price = generate_price(),
                        amount = generate_amount(),
                        date = today,
                        transaction_type = generate_transaction_type(),
                    )
                )
            today -= timedelta(days=1)
    
    Transaction.objects.bulk_create(transactions_to_create)