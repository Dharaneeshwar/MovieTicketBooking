from django.urls import path 
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('success/',views.success,name="success"),
    path('mybooking/',views.mybooking,name="bookingHistory"),
]