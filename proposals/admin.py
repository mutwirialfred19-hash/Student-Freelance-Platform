from django.contrib import admin
from .models import Proposal

@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    list_display = ['student', 'project', 'proposed_price', 'status', 'submitted_at']
    list_filter = ['status']
    search_fields = ['student__username', 'project__title']
