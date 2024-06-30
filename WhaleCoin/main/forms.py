from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('telegram_id', 'telegram_username', 'referral_code')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('telegram_id', 'telegram_username', 'coins', 'last_mining_start', 'referral_code', 'referred_by')