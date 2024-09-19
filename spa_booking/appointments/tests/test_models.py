from django.test import TestCase
from appointments.models import Service, ServiceProvider, Customer, Booking
from django.utils import timezone
from django.core.exceptions import ValidationError

class BookingModelTestCase(TestCase):
    
    def setUp(self):
        # Create a test service
        self.service = Service.objects.create(
            name='Facial',
            description='A relaxing facial session.',
            duration=60,
            price=100.00
        )
        
        # Create a test service provider
        self.service_provider = ServiceProvider.objects.create(
            first_name='Jane',
            last_name='Smith',
            gender='F',
            phone='1234567890',
            email='jane.smith@example.com',
            start_date='2024-11-01'
        )
        
        # Create a test customer
        self.customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone='0987654321'
        )

    def test_create_booking(self):
        """Test creating a booking with valid data"""
        # Create a booking instance
        booking = Booking.objects.create(
            service=self.service,
            service_provider=self.service_provider,
            customer=self.customer,
            date=timezone.now().date(),
            time=timezone.now().time()
        )

        # Assertions
        self.assertEqual(booking.service, self.service)
        self.assertEqual(booking.service_provider, self.service_provider)
        self.assertEqual(booking.customer, self.customer)
        self.assertIsNotNone(booking.created_at)
        self.assertIsNotNone(booking.updated_at)

    def test_booking_str(self):
        """Test the string representation of a booking"""
        booking = Booking.objects.create(
            service=self.service,
            service_provider=self.service_provider,
            customer=self.customer,
            date=timezone.now().date(),
            time=timezone.now().time()
        )
        
        expected_str = f"Booking for {self.customer} on {booking.date} at {booking.time}"
        self.assertEqual(str(booking), expected_str)

    def test_create_booking_missing_fields(self):
        """Test creating a booking with missing fields"""
        # Missing 'service' and 'service_provider' fields
        with self.assertRaises(ValidationError):
            booking = Booking(
                customer=self.customer,
                date=timezone.now().date(),
                time=timezone.now().time()
            )
            booking.full_clean()  # This will raise a ValidationError because of missing fields
            booking.save()
