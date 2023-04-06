from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg

from datetime import timedelta

min_value = 4300000000000000
max_value = 4399999999999999

class Card(models.Model):
    
    CHOICES = {
        ('purple', 'purple'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('orange', 'orange')
    }
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cards')
    card_name = models.CharField(max_length=40)
    card_holder = models.CharField(max_length=60)
    card_number = models.IntegerField(validators=[MinValueValidator(min_value), MaxValueValidator(max_value)])
    bank_name = models.CharField(max_length=80)
    valid_date = models.DateField()
    color = models.CharField(max_length=10, choices=CHOICES, default='purple')
    balance = models.FloatField(default=15000)
    
    def __str__(self):
        return self.card_name
    
class Coin(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='coins')
    
    def __str__(self):
        return self.name
    
    def get_last_day(self):
        return self.transactions.all().order_by('-date').first().date.date()
    
    def get_price_by_date(self, date):
        # get all transactions of a given date, and return average price
        return self.transactions.filter(date__date=date).aggregate(average=Avg('price'))['average']
            
    def get_last_five_days_data(self):
        last_day = self.get_last_day()
        data = []
        for i in range(1, 6):
            data.append(self.get_price_by_date(last_day))
            last_day -= timedelta(days=1)
        return data
    
    def get_last_day_price(self):
        # get last day avarage price
        last_day = self.get_last_day()
        last_day_transactions = self.transactions.filter(date__date=last_day)
        return last_day_transactions.aggregate(average = Avg('price'))['average']
    
    def get_performance_of_week(self, end_date):
        week_price = 0
        for i in range(0,7):
            week_price += self.get_price_by_date(end_date)
            end_date -= timedelta(days=1)
        week_price /= 7
        return week_price, end_date

    def get_performance(self):
        # get performance from last two weeks to calculate percentual growth between them
        last_day = self.get_last_day()
        current_week_price, last_day = self.get_performance_of_week(last_day) 
        last_week_price, last_day = self.get_performance_of_week(last_day)
        
        return round((current_week_price - last_week_price) / (last_week_price) * 100, 2)
    
    def get_last_day_performance(self):
        self.get_last_day()
        
    
    def get_last_transactions(self):
        if not self.transactions:
            return []
        return self.transactions.order_by('-date')[:7]


class Transaction(models.Model):
    
    CHOICE = (
        ('buy', 'buy'),
        ('sell', 'sell')
    )
    
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='transactions')
    price = models.FloatField()
    amount = models.FloatField()
    date = models.DateTimeField()
    transaction_type = models.CharField(max_length=4, choices=CHOICE)
    
    def __str__(self):
        return self.coin.name + ' ' + self.transaction_type + ' ' + str(self.date)
    
    @classmethod
    def get_last_day(cls):
        return cls.objects.all().order_by('-date').first().date.date()
    
    def get_total_price(self):
        return round(self.price * self.amount, 3)
    
class CoinCurrency(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='currency')
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='currency')
    amount = models.FloatField()
    
    class Meta:
        verbose_name = 'currency'
        verbose_name_plural = 'currencies'
    
    def get_total_price(self):
        return self.coin.get_last_day_price() * self.amount