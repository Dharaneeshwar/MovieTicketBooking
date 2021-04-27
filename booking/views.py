from django.shortcuts import render
from home.models import Show
from .models import Booking, Seat
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse

# Create your views here.

def bookShow(request,id):
    show = Show.objects.get(pk = id)
    context = {
        'movie': show.movie,
        'show':show
    }
    return render(request,'booking/bookShow.html',context)

def getBookings(request,id):
    show = Show.objects.get(pk = id)
    
    bookedSeats = set() 
    
    prevBookings = Seat.objects.filter(show = show)
    for booking in prevBookings:
        bookedSeats.add(booking.seat_no)
    context = {
        'bookedSeats':list(bookedSeats)
    }
    return JsonResponse(context)

def bookSeats(request,id):
    show = Show.objects.get(pk = id)
    bookingID = None
    if request.method == "POST":
        try:
            noOfPerson = request.POST.get('noOfPerson',0)
            totalPrice = request.POST.get('total',0)
            bookedSeats = request.POST.getlist('seatsBooked[]')
            newBooking = Booking(show = show,noOfPerson =noOfPerson,ticket_price = totalPrice,user = request.user.username)
            newBooking.save()
            bookingID = newBooking.id
            for seat in bookedSeats:
                tempseat = Seat(show = show,seat_no = seat,bookingId = newBooking)
                tempseat.save()
        except:
            bookingToBeDeleted = Booking.objects.get(pk = bookingID)
            bookingToBeDeleted.delete() 
            return JsonResponse({'status':False})
    else:
        return JsonResponse({'status':False})
    return JsonResponse({'status':True})