from django.shortcuts import render
from .models import Room, check_dispo
from django.views.generic import ListView
from datetime import datetime

# Create your views here.
def MainPage(request):
    return render(request, 'index.html')

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
