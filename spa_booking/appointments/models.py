from django.db import models

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


