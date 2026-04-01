from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "amount_paid", "date_paid")
    list_filter = ("date_paid",)
    search_fields = ("student_id",)
