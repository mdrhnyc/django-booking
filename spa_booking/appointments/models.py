from django.db import models
from rest_framework import serializers

# Create your models here.
class Service(models.Model):
    DURATION_CHOICES = [
        (60, '60 minutes'),
        (90, '90 minutes')
    ]

    id = models.AutoField(primary_key=True)  # Auto-generated ID field
    name = models.CharField(max_length=100)  # Name of the service
    description = models.TextField(blank=True)  # Detailed description of the service (optional)
    duration = models.IntegerField(choices=DURATION_CHOICES)  # Duration, limited to 60 or 90 minutes
    price = models.DecimalField(max_digits=5, decimal_places=2)  # Price for the service

    class Meta:
        unique_together = ('name', 'duration')  # Ensure name-duration pair is unique

    def __str__(self):
        return f"{self.name} ({self.duration} mins) - ${self.price:.2f}"


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price', 'duration', 'description']

class ServiceProvider(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    start_date = models.DateField()

    class Meta:
        # Example of optional Meta settings
        ordering = ['first_name', 'last_name']  # Orders by first name, then last name by default
        verbose_name = 'Service Provider'  # Custom name in the admin panel
        verbose_name_plural = 'Service Providers'  # Plural name in the admin panel

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceProvider
        fields = ['id', 'first_name', 'last_name', 'gender', 'phone', 'email', 'start_date']


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Ensure email is unique
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service_provider = models.ForeignKey(ServiceProvider, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()  # Date of the booking
    time = models.TimeField()  # Time of the booking
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set when the booking is created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set to now every time the booking is updated

    def __str__(self):
        return f"Booking for {self.customer} on {self.date} at {self.time}"


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
