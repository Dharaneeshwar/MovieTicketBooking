from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User , auth 
from home.models import Movie,Show
from .forms import MovieForm
# Create your views here.

def login(request):
    if request.method=="POST":
        username = request.POST['email'] 
        password = request.POST['Password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            if user.is_superuser:
                return redirect('/admin/movies')
            print("success")
            return redirect('/')
        else:
            print("invalid")
            return redirect('login')     
    else:    
        return render(request,'admin/login.html')

def showMovies(request):
    movie = Movie.objects.all()
    context = {
        'movies':movie
    }
    return render(request,'admin/showMovies.html',context)

def addMovies(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            return redirect('../')
        else:
            print("invalid form")   
    else:
        form = MovieForm()     
    return render(request,'admin/addMovie.html',{'form':form.as_p()}) 


def editMovie(request,id):
    movie = Movie.objects.get(id = id)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES,instance = movie)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            return redirect('../')
        else:
            print("invalid")   
    else:
        form = MovieForm(instance = movie)     
    return render(request,'admin/editMovie.html',{'form':form.as_p()})

def deleteMovie(request,id):
    movie = Movie.objects.filter(pk=id)
    movie.delete()
    return redirect('../')