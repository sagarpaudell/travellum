from django.db import models
from datetime import datetime
from accounts.models import User
from places.models import Place
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

class History(models.Model):
    traveller = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="user_traveller")
    guide = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="user_guide")
    place = models.ForeignKey(Place, on_delete= models.DO_NOTHING, blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    tour_complete = models.BooleanField(default = False)
    start_date = models.DateTimeField(default=datetime.now(), blank=True)
    end_date = models.DateTimeField(default=datetime.now(), blank=True)
    no_of_people = models.IntegerField(blank=True, default =1)
    no_of_children = models.IntegerField(blank=True, default=0)
    total_hours = models.IntegerField(blank=True)
    total_price = models.IntegerField(blank=True)
    def __str__(self):
        return self.traveller.first_name