from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import mark_safe
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'full_name', 'email', 'role_badge', 'is_active', 'date_joined']
    list_filter = ['role', 'is_active', 'email_verified']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    fieldsets = UserAdmin.fieldsets + (
        ('KCA Talent Hub', {'fields': ('role', 'email_verified', 'phone', 'avatar')}),
    )

    @admin.display(description='Name')
    def full_name(self, obj):
        return obj.get_full_name()

    @admin.display(description='Role')
    def role_badge(self, obj):
        colors = {'student': '#6366f1', 'client': '#10b981'}
        color = colors.get(obj.role, '#888')
        return mark_safe(f'<span style="background:{color};color:white;padding:2px 10px;border-radius:12px;font-size:11px">{obj.get_role_display()}</span>')
