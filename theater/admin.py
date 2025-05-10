from django.contrib import admin
from .models import Theaters,Showtimes,Seats
# Register your models here.

@admin.register(Theaters)
class TheatersAdmin(admin.ModelAdmin):
    list_display = ['id','name','city','address','manager']

@admin.register(Showtimes)
class ShowtimesAdmin(admin.ModelAdmin):
    list_display = ['id','movie','theater','show_time','screen_number']

@admin.register(Seats)
class SeatsAdmin(admin.ModelAdmin):
    list_display = ['id','theater','screen_number','row_label','seat_number','seat_type']
