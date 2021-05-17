from django.urls import path
from .views import MainPage, RoomSearch, ReservationPage, confirmReservation, ReservationList, cancelReservation

urlpatterns = [
    path('', MainPage, name = 'main_page'),
    path('rooms', RoomSearch.as_view(), name = 'search_rooms'),
    path('rooms/<int:pk>/book', ReservationPage.as_view(), name = 'book_room'),
    path('rooms/book/confirm', confirmReservation, name = 'confirm_res'),
    path('rooms/book/cancel', cancelReservation, name = 'cancel_res'),
    path('reservations', ReservationList.as_view(), name = 'reservation_list')
]