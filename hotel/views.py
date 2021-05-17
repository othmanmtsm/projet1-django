from django.shortcuts import redirect, render, HttpResponse
from .models import Room, check_dispo, Reservation
from django.views.generic import ListView, DetailView
from datetime import datetime

# Create your views here.
def MainPage(request):
    if (request.user.is_authenticated) :
        return render(request, 'index.html')
    return redirect('/login')

class RoomSearch(ListView):
    model = Room
    template_name = 'rooms.html'
    context_object_name = 'rooms'

    def get_queryset(self):
        capacity = self.request.GET.get('cap')
        checkin = datetime.strptime(self.request.GET.get('chkin'), '%Y-%m-%d').date()
        checkout = datetime.strptime(self.request.GET.get('chkout'), '%Y-%m-%d').date()
        rooms = []
        for room in Room.objects.all():
            if check_dispo(room, checkin, checkout):
                rooms.append(room)
        return rooms

class ReservationPage(DetailView):
    model = Room
    context_object_name = 'room'
    template_name = 'reservation.html'

class ReservationList(ListView):
    model = Reservation
    template_name = 'reservations.html'

def confirmReservation(request):
    print(request.POST)
    print(request.GET)
    reservation = Reservation.objects.create(
        user = request.user,
        room = Room.objects.get(pk = int(request.POST.get('roomid'))),
        check_in = request.POST.get('chkin'),
        check_out = request.POST.get('chkout')
    )
    reservation.save()
    return HttpResponse('payment process ............')

def cancelReservation(request):
    Reservation.objects.filter(pk = int(request.POST.get('resid'))).delete()
    return HttpResponse('reservation canceled')