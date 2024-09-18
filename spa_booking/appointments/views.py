from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service, Booking, ServiceSerializer, BookingSerializer

# A simple API to get services
@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


# A simple API to get services
@api_view(['GET'])
def get_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)


