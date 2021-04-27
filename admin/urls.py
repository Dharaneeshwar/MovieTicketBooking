from django.urls import path 
from . import views

urlpatterns=[
    path('',views.login,name="admin-login"),
    path('movies/',views.showMovies,name="show-movies"),
    path('movies/add/',views.addMovies,name="add-movies"),
    path('movies/edit/<id>',views.editMovie,name="add-movies"),
    
]