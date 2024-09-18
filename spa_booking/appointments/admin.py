from django.contrib import admin
from .models import Service, ServiceProvider, Customer, Booking


# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'duration', 'price', 'description')  # Fields to display in the admin list view
    search_fields = ('name', 'description')  # Allow search by name and description
    list_filter = ('duration',)  # Filter by duration in the admin panel

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'phone', 'email', 'start_date')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('gender', 'start_date')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('email', 'phone')


@admin.register(Booking)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('service', 'service_provider', 'customer', 'date', 'time', 'created_at', 'updated_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'service__name')
    list_filter = ('date', 'service_provider', 'service')