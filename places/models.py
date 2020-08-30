from django.db import models
from datetime import datetime
from accounts.models import User 


class Place(models.Model):
    name = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)
    total_tours = models. IntegerField(default=0)

    def __str__(self):
        return self.name
   
class Review(models.Model):
    place_name = models.ForeignKey(Place,on_delete=models.CASCADE)
    Reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    place_review = models.TextField(blank=True)
    ratings = models.DecimalField(max_digits=2, decimal_places=1, blank=True)


