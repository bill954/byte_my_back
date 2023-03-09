from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import UserProfile

from django import forms

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = [
            'phone_number',
            'profile_image',
            'cover_image',
            'occupation',
            'description',
            'availability',
            'years_of_experience',
            'birth_date',
            'address',
            'company_name',
            'country',
            'language',
        ]