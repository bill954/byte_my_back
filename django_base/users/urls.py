from django.urls import path
from django.contrib.auth.views import LogoutView

from users.views import login_view, register, users_list_view, user_profile_view, block_user, delete_user

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(template_name = 'users/login.html'), name='logout'),
    path('register/', register, name='register'),
    path('users_list/', users_list_view, name='users_list'),
    path('user_profile/', user_profile_view, name='user_profile'),
    path('block/<int:user_id>/', block_user, name='block'),
    path('delete/<int:user_id>/', delete_user, name='delete'),
]