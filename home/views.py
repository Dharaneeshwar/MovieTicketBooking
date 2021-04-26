from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Movie, Show
from datetime import datetime, timedelta
# Create your views here.


def home(request):
    user = request.user
    if user.is_anonymous:
        return redirect('accounts/login/')
    # time_threshold = timedelta(days = 3) + datetime.now()
    # shows = Show.objects.all()
    shows = Show.objects.filter(date__range = [datetime.today(),datetime.today()+timedelta(2)]).order_by('date');
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