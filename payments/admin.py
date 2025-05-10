from django.contrib import admin
from .models import Payments
# Register your models here.

@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id','booking','amount','status','transaction_time']