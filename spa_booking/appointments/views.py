from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Service, ServiceSerializer

# A simple API to get services
@api_view(['GET'])
def get_services(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)


