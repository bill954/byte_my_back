from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

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
    
    def __str__(self):
        return self.card_name