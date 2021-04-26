from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    image = models.ImageField(blank= True,upload_to='./movie',default = 'default.jpg')
    ticket_price = models.FloatField()
    description = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.movie_name