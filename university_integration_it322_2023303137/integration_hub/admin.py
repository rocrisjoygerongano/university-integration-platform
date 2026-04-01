from django.contrib import admin
from .models import IntegrationLog

@admin.register(IntegrationLog)
class IntegrationLogAdmin(admin.ModelAdmin):
    list_display = ("source_system", "target_system", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("source_system", "target_system", "status")
