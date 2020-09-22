from django.db import models
from django.db.models.signals import post_save
from datetime import datetime
from travellers.models import Traveller
from accounts.models import User
from places.models import Place

class Guide(models.Model):
    email = models.OneToOneField(User,on_delete= models.CASCADE, unique=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=False)
    is_active = models.BooleanField(default = False)
    tours_count = models.IntegerField(default=0)
    driverlicense_front = models.ImageField(upload_to='photos/%Y%/%d/', blank=True)
    driverlicense_back = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    driverlicense_number = models.CharField(max_length=20,blank=True)
    citizenship_front = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    citizenship_back= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    citizenship_number = models.CharField(max_length=20,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    places = models.ManyToManyField(Place, blank=True)
    replies_within = models.IntegerField(default=1)

    def __str__(self):
        return self.email.email

    def get_place(self):
        return self.places.first()

class Guide_Review(models.Model):
    guide = models.ForeignKey(User, on_delete= models.CASCADE)
    guide_reviewer = models.ForeignKey(Traveller, on_delete= models.CASCADE)
    guide_review = models.TextField(blank=True)
    guide_ratings = models.IntegerField(blank=True)


class Transaction(models.Model):
    paid_by = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="payer")
    paid_to = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="earner")
    pid = models.CharField(blank=True, max_length=10)
    refId = models.CharField(blank=True, max_length=10)
    tamt = models.DecimalField(blank=True, decimal_places=4, max_digits=10)
    t_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.refId



def change_is_guide(sender, instance, **kwargs):
    """ function to receive signal from guide save"""
    t = Traveller.objects.get(email = instance.email)
    if instance.is_published :
        t.is_guide = True
        t.save()
        print('a guide entry was changed')
    else:
        t.is_guide = False
        t.save()
        print('a guide entry was changed')


#sends signal to change_is_guide when a new entry is saved in guide model
post_save.connect(change_is_guide, sender=Guide) 