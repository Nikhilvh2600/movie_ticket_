from django.shortcuts import render,redirect
from movies.models import Movies
from accounts.models import User 
from bookings.models import Bookings,BookingSeats
from payments.models import Payments
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Create your views here.

def home(request):
    movies = Movies.objects.all()
    context = {'movies':movies } 
    return render(request,'dashboard/home.html',context)

@login_required
def your_orders(request):
    user = User.objects.get(username=request.user)
    bookings = Bookings.objects.filter(user=user,booking_status='confirmed').order_by('-booking_time')
    tickets ={ Payments.objects.get(booking=booking):(BookingSeats.objects.filter(booking=booking),
                                                      check_cancellation(booking.showtime))
              for booking in bookings }
    context = {
                'tickets' : tickets,
               'user':user }
    return render(request,'dashboard/your_orders.html',context)
    
from django.utils.timezone import now
from datetime import timedelta
def check_cancellation(showtime):
    now_time = now()
    buffer_time = now_time + timedelta(minutes=20)
    return showtime.show_time > buffer_time

def search_view(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        movies = Movies.objects.filter(title__icontains=search_query)
        context = {'movies':movies }
        return render(request,'dashboard/search.html',context)
    return redirect('home')