from django.db import models
from django.conf import settings

# Create your models here.
class Room(models.Model):
    ROOM_TYPES = (
        ('Single', 'Single Room'),
        ('Double', 'Double Room'),
        ('Triple', 'Triple Room'),
        ('Quad', 'Quad Room'),
        ('Queen', 'Queen Room'),
        ('King', 'King Room'),
        ('Twin', 'Twin Room'),
        ('Studio', 'Studio Room')
    )

    num = models.IntegerField()
    roomType = models.CharField(max_length=10 ,choices=ROOM_TYPES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    remise3j = models.DecimalField(max_digits=6, decimal_places=2)
    remise8j = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.num} - {self.roomType} with {self.beds} beds for {self.capacity} people'

class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    room = models.ForeignKey(Room, on_delete= models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

def check_dispo(room, check_in, check_out):
    disp_list = []
    res_list = Reservation.objects.filter(room= room)
    for res in res_list:
        if res.check_in > check_out or res.check_out < check_in:
            disp_list.append(True)
        else:
            disp_list.append(False)
    return all(disp_list)