from django.contrib import admin
from django.utils.html import mark_safe
from .models import Project, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'client', 'category', 'status_badge', 'budget_min', 'budget_max', 'is_approved', 'created_at']
    list_filter = ['status', 'is_approved', 'category']
    list_editable = ['is_approved']
    search_fields = ['title', 'description']
    actions = ['approve', 'reject']

    @admin.display(description='Status')
    def status_badge(self, obj):
        colors = {'open': '#10b981', 'in_progress': '#f59e0b', 'completed': '#6366f1', 'cancelled': '#ef4444'}
        color = colors.get(obj.status, '#888')
        return mark_safe(f'<span style="background:{color};color:white;padding:2px 10px;border-radius:12px;font-size:11px">{obj.get_status_display()}</span>')

    @admin.action(description='Approve selected projects')
    def approve(self, request, queryset):
        queryset.update(is_approved=True)

    @admin.action(description='Reject selected projects')
    def reject(self, request, queryset):
        queryset.update(is_approved=False)
