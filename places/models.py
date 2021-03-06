from django.db import models
from datetime import datetime
from accounts.models import User 
from travellers.models import Traveller


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
    keywords = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Major_Attraction(models.Model):
    place = models.ForeignKey(Place, on_delete= models.DO_NOTHING, blank=True)
    attraction_name = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)

class Things_To_Do(models.Model):
    place = models.ForeignKey(Place, on_delete= models.DO_NOTHING, blank=True)
    task_name = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True)
   
class Review(models.Model):
    place_name = models.ForeignKey(Place,on_delete=models.CASCADE)
    Reviewer = models.ForeignKey(Traveller, on_delete=models.CASCADE)
    place_review = models.TextField(blank=True)
    ratings = models.IntegerField(blank=True)

    def __str__(self):
        return '%s %s' % (self.place_name ,self.Reviewer)
