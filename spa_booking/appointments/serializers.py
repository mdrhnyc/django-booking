from rest_framework import serializers
from .models import Service, ServiceProvider, Customer, Booking
from django.utils import timezone

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price', 'duration', 'description']


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id', 'first_name', 'last_name', 'gender', 'phone', 'email', 'start_date']


class BookingSerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name')
    customer_first_name = serializers.CharField(source='customer.first_name')
    customer_last_name = serializers.CharField(source='customer.last_name')
    service_provider_first_name = serializers.CharField(source='service_provider.first_name')
    service_provider_last_name = serializers.CharField(source='service_provider.last_name')


    class Meta:
        model = Booking
        fields = ['id', 'service_name', 'customer_first_name', 'customer_last_name', 'service_provider_first_name', 'service_provider_last_name', 'date', 'time']


# appointments/serializers.py
class BookingCreateSerializer(serializers.ModelSerializer):
    customer_first_name = serializers.CharField(write_only=True)
    customer_last_name = serializers.CharField(write_only=True)
    customer_email = serializers.EmailField(write_only=True)

    class Meta:
        model = Booking
        fields = ['service', 'service_provider', 'date', 'time', 'customer_first_name', 'customer_last_name', 'customer_email']

    def create(self, validated_data):
        # Extract customer data from the validated data
        customer_first_name = validated_data.pop('customer_first_name')
        customer_last_name = validated_data.pop('customer_last_name')
        customer_email = validated_data.pop('customer_email')
        

        # Create or retrieve the customer by email (ensure uniqueness)
        customer, created = Customer.objects.get_or_create(
            email=customer_email,
            defaults={
                'first_name': customer_first_name,
                'last_name': customer_last_name
            }
        )

        # Create booking with the customer
        booking = Booking.objects.create(customer=customer, **validated_data)
        return booking

    def validate(self, data):
        service = data['service']
        service_provider = data['service_provider']

        booking_date = data['date']
        booking_time = data['time']

        # Calculate the start and end times for the booking
        booking_start = timezone.make_aware(timezone.datetime.combine(booking_date, booking_time))
        booking_end = booking_start + timezone.timedelta(minutes=service.duration)

        # Check if the service provider is booked for the same or overlapping time
        overlapping_bookings = Booking.objects.filter(
            service_provider=service_provider,
            date=booking_date,
            time__lt=booking_end.time(),  # End time of an existing booking
            time__gte=booking_start.time()  # Start time of an existing booking
        )

        if overlapping_bookings.exists():
            raise serializers.ValidationError({"message": "The service provider is already booked during this time."})

        return data