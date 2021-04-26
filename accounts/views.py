from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.models import User , auth 
# Create your views here.

def login(request):
    if request.method=="POST":
        print("inside login post")
        username = request.POST['email'] 
        password = request.POST['Password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            print("success")
            return redirect('/')
        else:
            print("invalid")
            return redirect('login')     
    else:    
        return render(request,'accounts/login.html')

def register(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        lastname=request.POST['last_name']
        username = request.POST['email'] 
        password1 = request.POST['password1'] 
        password2 = request.POST['password2']
        email = request.POST['email'] 

        if password1==password2:
            if User.objects.filter(username=username).exists():
                pass
            else:    
                user = User.objects.create_user(username=username,password=password1, email=email, first_name=first_name,last_name = lastname)
                user.save()
                # print("user created")
                return redirect("/")
        else:
            messages.info(request,"Password didn't match")

            print("password not match")    
    return render(request,'accounts/register.html')

def logout(request):
    print("logout")
    auth.logout(request)
    return  HttpResponseRedirect(reverse('login'))

def tologin(request):
    return  HttpResponseRedirect(reverse('login'))

def toregister(request):
    return HttpResponseRedirect(reverse('register'))    

