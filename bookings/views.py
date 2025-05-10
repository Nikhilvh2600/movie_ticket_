from django.shortcuts import render,redirect
from theater.models import Theaters,Seats,Showtimes
from accounts.models import User 
from movies.models import Movies
from datetime import datetime, timedelta,date
import json
from .models import Bookings,BookingSeats
from django.http import JsonResponse,HttpResponse
from django.conf import settings
import stripe
from django.contrib.auth.decorators import login_required
from django.contrib import messages

stripe.api_key = settings.STRIPE_SECRET_KEY
# Create your views here.

# def theater_show_time_view(request,slug):
#     today = datetime.today().date()
#     start_date = today - timedelta(days=0) 
#     week = []
#     for i in range(7):
#         day = start_date + timedelta(days=i)
#         week.append({
#             'name': day.strftime("%a").upper(),
#             'day': day.day,
#             'month': day.strftime("%b").upper(),
#             'date': day
#         })
#     if Movies.objects.filter(slug=slug).exists():
#         movie = Movies.objects.get(slug=slug)
#         theater_showtimes = [
#              Showtimes.objects.filter(movie=movie,theater=theater).order_by('show_time')
#             for theater in Theaters.objects.all() if Showtimes.objects.filter(movie=movie,theater=theater).exists() ]
#         context = {
#             'theater_showtimes':theater_showtimes,
#             'week': week,
#             'today': today,
#             'slug' : slug
#         }
#         return render(request,'theater/theater_showtimes_list.html',context)
    
#     return render(request, 'movies/404.html')











@login_required
def theater_sow_time_selceted_date_view(request,slug,date_str):
    try:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        selected_date = datetime.today().date()
    today = datetime.today().date()
    start_date = today - timedelta(days=0) 
    week = []
    for i in range(7):
        day = start_date + timedelta(days=i)
        week.append({
            'name': day.strftime("%a").upper(),
            'day': day.day,
            'month': day.strftime("%b").upper(),
            'date': day
        })
    if Movies.objects.filter(slug=slug).exists():
        movie = Movies.objects.get(slug=slug)
        theater_showtimes = [
             Showtimes.objects.filter(movie=movie,theater=theater,
                                      show_time__date=selected_date).order_by('show_time')
            for theater in Theaters.objects.all() if Showtimes.objects.filter(movie=movie,theater=theater,
                                                                            show_time__date=selected_date).exists() ]
        context = {
            'theater_showtimes':theater_showtimes,
             'week': week,
             'today': selected_date,
             'slug' : slug,
             'movie' : movie
        }
        return render(request,'theater/theater_showtimes_list.html',context)
    
    return render(request, 'movies/404.html')



def seat_selection_view(request, showtime_id):
    showtime = Showtimes.objects.get(id=showtime_id)
    all_seats = Seats.objects.filter(
        theater=showtime.theater,
        screen_number=showtime.screen_number
    ).order_by('row_label', 'seat_number')
    booking = Bookings.objects.filter(showtime=showtime)
    booked_seats = [booked_seat.seat for booked_seat in BookingSeats.objects.filter(booking__in=booking)]
    seat_rows = {}
    
    for seat in all_seats:
        
        row = (seat.row_label,seat.seat_type)
        if row not in seat_rows:
            seat_rows[row] = []
        if seat not in booked_seats:
            seat_rows[row].append(seat)
        else: 
            seat_rows[row].append(0)
    context = {
        'showtime': showtime,
        'seat_rows': seat_rows,
        
    }
    return render(request, 'theater/seating.html',
                   context)



@login_required 
def book_ticket_view(request,showtime_id):
    convenience_fee = 49
    if request.method == 'POST':
        selected_seats = json.loads( request.POST['selected_seats'])
        total_amount =int(request.POST['total_amount'])
        tickets = []
        showtime = Showtimes.objects.get(id=showtime_id)
        user = User.objects.get(username=request.user)
        booking = Bookings.objects.create(
            user=user,
            showtime=showtime,
            total_amount = total_amount + convenience_fee,
            booking_status = 'pending'
        )
        for seat in selected_seats:
            tickets.append(seat['key'])
            seat_id = seat['id']
            seat_obj = Seats.objects.get(id = seat_id)
            BookingSeats.objects.create(
              booking=booking,
              seat=seat_obj  
            )
        context = {
            'convenience_fee' : convenience_fee,
            'showtime' : showtime,
            'total_amount' : total_amount,
            'sub_total':total_amount+ convenience_fee,
            'tickets' : tickets,
            'booking' : booking,
            'stripe_public_key': settings.STRIPE_PUBLIC_KEY


        }
        return render(request,'payments/proceed_to_payment.html',context)
    return HttpResponse('Invalid Request')

@login_required
def cancel_booking(request,booking_id):
    booking = Bookings.objects.get(id=booking_id)
    booking.booking_status = 'cancelled'
    booking.save()
    qs = BookingSeats.objects.filter(booking=booking)
    qs.delete()
    messages.error(request,'your booking have been cancelled amount refunded to your bank account')
    return redirect('your_orders')