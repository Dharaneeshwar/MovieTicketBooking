from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Movie
# from ..accounts.views import login
# Create your views here.


def home(request):
    user = request.user
    if user.is_anonymous:
        return redirect('accounts/login/')
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'home/dashboard.html', context)
