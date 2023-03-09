from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

from users.forms import RegisterForm, UserProfileForm
from users.models import UserProfile

from admin_settings.models import Country, Language

def login_view(request):
    if request.method == 'GET':
        return render(request, 'users/login.html')
    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('index')
            
        else:
            context = {
                'errors': form.errors,
            }
            return render(request, 'users/login.html', context)
        
def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = {
                'errors': form.errors,
            }
            return render(request, 'users/register.html', context)
        
def users_list_view(request):
    return render(request, 'users/users_list.html')

def user_profile_view(request):
    if request.method == 'GET':
        context = {
            'languages': Language.objects.all(),
            'countries': Country.objects.all(),
        }
        return render(request, 'users/user_profile.html', context)
    elif request.method =='POST':
        
        data = request.POST.copy()
        
        if request.POST.get('country') and Country.objects.filter(name = request.POST.get('country')).exists:
            country = Country.objects.get(name = request.POST.get('country'))
            data['country'] = country.id

        if request.POST.get('language') and Language.objects.filter(name = request.POST.get('language')).exists:
            language = Language.objects.get(name = request.POST.get('language'))
            data['language'] = language.id
            
        form = UserProfileForm(data, request.FILES, instance=request.user.profile)
        
        print(data)
        
        if form.is_valid():
            form.save()
            return redirect('user_profile')
        else:
            context = {
                'errors': form.errors,
                'languages': Language.objects.all(),
                'countries': Country.objects.all(),
            }
            return render(request, 'users/user_profile.html', context)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user = instance)
