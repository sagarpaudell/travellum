from django.db import models
from datetime import datetime
from accounts.models import User

class Traveller(models.Model):
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    email = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True)
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    bio = models.TextField(blank=True)    
    contact_no = models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=2,blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    tours_count = models. IntegerField(default=0)
    is_guide = models.BooleanField(default=False)
    price_per_hour= models.DecimalField(max_digits=5,default=0,decimal_places = 2)
    def __str__(self):
        return self.first_name