from django.shortcuts import render,redirect
from bookings.models import Bookings
from django.conf import settings
from .models import Payments
from accounts.models import User
import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

def payment_page(request,booking_id):
    booking = Bookings.objects.get(id = booking_id)
    if request.method == 'POST':
        booking = Bookings.objects.get(id = booking_id) 
        session = stripe.checkout.Session.create(  
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': 'Ticket Booking',
                    },
                    'unit_amount': int(booking.total_amount*100),
                },
                'quantity': 1,
            }],
            mode='payment', 
            billing_address_collection='required', 
            success_url=f'http://127.0.0.1:8000/payments/success/{booking.id}/',
            cancel_url=f'http://127.0.0.1:8000/payments/cancel/{booking.id}/',
        )
        return redirect(session.url, code=303)

    return render(request, 'payments/payment.html', {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY,
        'booking' : booking
    })


def success(request,booking_id):
    booking = Bookings.objects.get(id=booking_id)
    booking.booking_status = 'confirmed'
    booking.save()
    Payments.objects.create(booking=booking,payment_method='card'
                            ,amount=booking.total_amount,status='success')
    return render(request,'payments/success.html')

def cancel(request,booking_id):
    booking = Bookings.objects.get(id=booking_id)
    booking.booking_status = 'cancelled'
    booking.save()
    Payments.objects.create(booking=booking,payment_method='card'
                            ,amount=booking.total_amount,status='failed')
    return render(request,'payments/cancel.html') 