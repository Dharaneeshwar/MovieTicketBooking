from django.db import models
from home.models import Show
# Create your models here.

class Booking(models.Model):
    show = models.ForeignKey(Show,on_delete=models.CASCADE)
    noOfPerson = models.IntegerField()
    ticket_price = models.FloatField()
    user = models.CharField(max_length=500,default="")
    def __str__(self):
        return str(self.ticket_price)+" , "+str(self.noOfPerson)

class Seat(models.Model):
    show = models.ForeignKey(Show,on_delete=models.CASCADE)
    seat_no = models.IntegerField();
    bookingId = models.ForeignKey(Booking,on_delete=models.CASCADE)
