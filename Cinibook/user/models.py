from django.db import models
from django.contrib.auth.models import User 

ITEM = [
    ('1','1'),
    ('2','2'),
    ('3','3')
]

class Movie(models.Model):
    image=models.ImageField(upload_to='images/',blank=True)
    name=models.CharField(max_length=50)
    disc=models.CharField(max_length=70)
    def __str__(self):
        return self.name
    
class Database(models.Model): 
    c_name = models.ForeignKey(User, on_delete=models.CASCADE)
    c_moviename=models.ManyToManyField(Movie) 
    c_count=models.TextField(max_length=2, choices=ITEM)
    c_date=models.DateField()
class Booking(models.Model):
    user=models.TextField(max_length=200,default="")
    name=models.TextField(max_length=100)
    ticket=models.IntegerField()
    date=models.DateField(default="")
    def __str__(self):
        return self.name