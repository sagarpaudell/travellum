from django.db import models
from datetime import datetime
from travellers.models import Traveller
from accounts.models import User
from places.models import Place

class Guide(models.Model):
    email = models.ForeignKey(User,on_delete= models.CASCADE)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
    tours_count = models.IntegerField(default=0)
    citizenship_front = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    citizenship_back= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    citizenship_number = models.CharField(max_length=20,blank=True)
    reviews = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=True)
    places = models.ManyToManyField(Place)

    def __str__(self):
        return self.email.email