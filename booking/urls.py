from django.urls import path 
from . import views

urlpatterns=[
    path('show/<id>',views.bookShow,name="home"),
    path('show/<id>/getBookings',views.getBookings,name="home"),
    path('show/<id>/bookSeats',views.bookSeats,name="home"),
]