from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service, Booking, ServiceProvider, ServiceSerializer, BookingSerializer, ServiceProviderSerializer, BookingCreateSerializer
from .utils import send_confirmation_email 

# A simple API to get services
@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


# A simple API to get bookings
@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_booking_view(request):
    if request.method == 'POST':
        serializer = BookingCreateSerializer(data=request.data)
        if serializer.is_valid():
            booking = serializer.save()
            
            customer_email = booking.customer.email  # Adjust based on your serializer fields
            booking_details = f"Booking ID: {booking.id}\nService: {booking.service}\nDate: {booking.date}\nTime: {booking.time}"
            
            send_confirmation_email(customer_email, booking_details)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# A simple API to get service providers
@api_view(['GET'])
def get_service_providers(request):
    serviceproviders = ServiceProvider.objects.all()
    serializer = ServiceProviderSerializer(serviceproviders, many=True)
    return Response(serializer.data)


