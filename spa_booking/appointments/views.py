from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service, Booking, ServiceProvider, ServiceSerializer, BookingSerializer, ServiceProviderSerializer

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

# A simple API to get service providers
@api_view(['GET'])
def get_service_providers(request):
    serviceproviders = ServiceProvider.objects.all()
    serializer = ServiceProviderSerializer(serviceproviders, many=True)
    return Response(serializer.data)


