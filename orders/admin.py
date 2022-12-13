from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


# We can use TabularInline or StackedInline in admin to display comments in product line 
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    fields = ['order', 'product', 'quantity', 'price']
    extra = 1

@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid',]
    
    inlines = [
        OrderItemInline,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price']

