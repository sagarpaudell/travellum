from django.db import models
from datetime import datetime
from accounts.models import User
from places.models import Place
from django.core.validators import MaxValueValidator, MinValueValidator

class History(models.Model):
    traveller = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="user_traveller")
    guide = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="user_guide")
    place = models.ForeignKey(Place, on_delete= models.DO_NOTHING, blank=True)
    guide_review = models.TextField(blank=True)
    guide_rating = models.IntegerField(blank=True, validators=[MaxValueValidator(5), MinValueValidator(0)])
    traveller_review = models.TextField(blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.place
