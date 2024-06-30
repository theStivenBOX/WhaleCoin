from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import string
import random

def generate_referral_code():
    length = 10
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class CustomUserManager(BaseUserManager):
    def create_user(self, telegram_id, username=None, referral_code=None, **extra_fields):
        if not telegram_id:
            raise ValueError('The Telegram ID must be set')
        user = self.model(telegram_id=telegram_id, username=username, **extra_fields)
        user.referral_code = generate_referral_code()
        if referral_code:
            try:
                referrer = CustomUser.objects.get(referral_code=referral_code)
                user.referred_by = referrer
                user.save(using=self._db)
                self._assign_referrals(user, referrer)
            except CustomUser.DoesNotExist:
                pass
        user.save(using=self._db)
        return user

    def _assign_referrals(self, user, referrer):
        current_level = 1
        while referrer and current_level <= 5:
            referrer.referrals.add(user)
            referrer = referrer.referred_by
            current_level += 1

    def create_superuser(self, telegram_id, username=None, **extra_fields):
        raise NotImplementedError('No superuser creation supported')

class CustomUser(AbstractUser):
    telegram_id = models.CharField(max_length=100, unique=True)
    telegram_username = models.CharField(max_length=50, blank=True, null=True)
    coins = models.IntegerField(default=0)
    last_mining_start = models.DateTimeField(null=True, blank=True)
    referral_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    referred_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='referrals')

    objects = CustomUserManager()

    USERNAME_FIELD = 'telegram_id'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'custom_user'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Уникальное related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Уникальное related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.telegram_id
    
    def get_referrals_at_level(self, level):
        if level == 1:
            return self.referrals.all()
        elif level > 1:
            referrals = self.referrals.all()
            for _ in range(level - 1):
                referrals = CustomUser.objects.filter(referred_by__in=referrals)
            return referrals
        return CustomUser.objects.none()

    def count_referrals_at_level(self, level):
        return self.get_referrals_at_level(level).count()