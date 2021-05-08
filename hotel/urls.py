from django.urls import path
from .views import MainPage, RoomSearch

urlpatterns = [
    path('', MainPage, name = 'main_page'),
    path('rooms', RoomSearch.as_view(), name = 'search_rooms'),
]