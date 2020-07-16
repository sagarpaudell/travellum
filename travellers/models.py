from django.db import models
from datetime import datetime

class Traveller(models.Model):
    name = models.CharField(max_length=200)
    #email = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    bio = models.TextField(blank=True)    
    contact_no = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    tours_count = models. IntegerField(default=0)
    def __str__(self):
        return self.email