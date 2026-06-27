from django.contrib import admin
from .models import StudentProfile, ClientProfile

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'university', 'course', 'year_of_study', 'is_available', 'jobs_completed']
    search_fields = ['user__username', 'user__first_name', 'skills']

@admin.register(ClientProfile)
class ClientProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'industry', 'location']
