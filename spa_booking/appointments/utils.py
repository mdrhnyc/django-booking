from django.core.mail import send_mail

def send_confirmation_email(customer_email, booking_details):
    subject = 'Booking Confirmation'
    message = f'Thank you for your booking!\n\nDetails:\n{booking_details}'
    from_email = 'your-email@example.com'
    recipient_list = [customer_email]
    
    send_mail(subject, message, from_email, recipient_list)
