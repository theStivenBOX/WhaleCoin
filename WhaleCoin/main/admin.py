from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('telegram_id', 'telegram_username', 'coins', 'last_mining_start', 'referral_code', 'referred_by')
    fieldsets = (
        (None, {'fields': ('telegram_id', 'telegram_username', 'password')}),
        ('Personal info', {'fields': ('coins', 'last_mining_start', 'referral_code', 'referred_by')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('telegram_id', 'telegram_username', 'password1', 'password2', 'referral_code', 'referred_by', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    search_fields = ('telegram_id', 'telegram_username')
    ordering = ('telegram_id',)

admin.site.register(CustomUser, CustomUserAdmin)

