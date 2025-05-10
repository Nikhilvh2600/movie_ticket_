from django.db import models
from accounts.models import User
from movies.models import Movies
# Create your models here.

class Theaters(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL,
                                null=True,blank=True)
    def __str__(self):
        return self.name

class Showtimes(models.Model):
    movie = models.ForeignKey(Movies,on_delete=models.SET_NULL,
                              null=True,blank=True)
    theater = models.ForeignKey(Theaters,on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    screen_number = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'{self.movie} {self.show_time}'

class Seats(models.Model):
    theater = models.ForeignKey(Theaters,on_delete=models.CASCADE)
    screen_number = models.IntegerField(null=True,blank=True)
    row_label = models.CharField(max_length=10)
    seat_number = models.IntegerField()
    seat_type = models.CharField(max_length=20,choices=[['gold','Gold'],
                                                        ['silver','Silver']])
    def __str__(self):
        return f'{self.row_label}{self.seat_number} {self.theater}  {self.seat_type}'