from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Movie, Show
from datetime import datetime, timedelta
from booking.models import Booking
# Create your views here.


def home(request):
    user = request.user
    if user.is_anonymous:
        return redirect('accounts/login/')
    shows = Show.objects.filter(date__range = [datetime.today(),datetime.today()+timedelta(2)]).order_by('date').order_by('timing');
    all_show_info = []
    for show in shows:
        movie = show.movie
        show_info = {}
        show_info['show'] = show
        show_info['movie'] = movie 
        show_info['id'] = show.id 
        all_show_info.append(show_info)
    context = {
        'shows': all_show_info
    }
    return render(request, 'home/dashboard.html', context)

def success(request):
    return render(request,'booking/success.html')

def mybooking(request):
    user = request.user
    bookingQuery = Booking.objects.filter(user = user.username)
    booking = []
    for book in bookingQuery:
        temp = {}
        temp['booking'] = book 
        temp['movie'] = book.show.movie.movie_name 
        temp['perHead'] = book.ticket_price/book.noOfPerson
        booking.append(temp)
    print(booking)
    context = {
        'bookings':booking
    }
    return render(request,'home/booking_history.html',context)