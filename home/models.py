from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    image = models.ImageField(blank= True,upload_to='./movie',default = 'default.jpg')
    ticket_price = models.FloatField()
    description = models.CharField(max_length=500,default="")
    def __str__(self):
        return self.movie_name

class Show(models.Model):
    SCREEN = (('A','A'),('B','B'),('C','C'),('D','D'))
    TIMING = (('10AM','10AM'),('1PM','1PM'),('4PM','4PM'),('7PM','7PM'))
    movie =  models.ForeignKey(Movie,on_delete=models.CASCADE)
    screen = models.CharField(max_length=5,choices=SCREEN)
    timing = models.CharField(max_length=5,choices=TIMING)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.screen

    class Meta:
        unique_together = ('screen', 'timing','date',)