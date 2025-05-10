from django.urls import path 
from . import views 

urlpatterns = [
    # path('theater-showtime/<slug>/',views.theater_show_time_view,name='theater_showtime'),
    path('theater-showtime/<slug>/<date_str>/',views.theater_sow_time_selceted_date_view,name='theater_showtime_date'),
    path('seat-selection/<int:showtime_id>/',views.seat_selection_view,name="select_seats"),
    path('book-ticket/<int:showtime_id>/',views.book_ticket_view,name='book_ticket'),
    path('canel-booking/<int:booking_id>/',views.cancel_booking,name='cancel_booking')
]