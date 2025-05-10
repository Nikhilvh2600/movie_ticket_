from django.contrib import admin
from .models import Bookings,BookingSeats
# Register your models here.


@admin.register(Bookings)
class BookingAdmin(admin.ModelAdmin):
    list_display = [ 'id','user','showtime','total_amount','booking_status','booking_time']

@admin.register(BookingSeats)
class BookingSeatsAdmin(admin.ModelAdmin):
    list_display = ['id','booking','seat']