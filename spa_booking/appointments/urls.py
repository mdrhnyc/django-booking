from django.urls import path
from .views import get_services, get_bookings, get_service_providers, create_booking_view

urlpatterns = [
    path('api/services/', get_services, name='get_services'),
    path('api/bookings/', get_bookings, name='get_bookings'),
    path('api/booking/', create_booking_view, name='create_booking_view'),
    path('api/service-providers/', get_service_providers, name='get_service_providers'),
]
