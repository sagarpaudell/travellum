from django.db import models
from datetime import datetime
from accounts.models import User
from chat.models import Chat
from PIL import Image


class Traveller(models.Model):
    first_name = models.CharField(max_length=200,blank=True)
    last_name = models.CharField(max_length=200,blank=True)
    email = models.OneToOneField(User, on_delete= models.CASCADE, blank=True)
    address = models.CharField(max_length=200,blank=True)
    city = models.CharField(max_length=100,blank=True)
    country = models.CharField(max_length=100,blank=True)
    bio = models.TextField(blank=True)
    social = models.TextField(blank=True) 
    slogan = models.CharField(max_length=1000,blank=True)   
    languages = models.CharField(max_length=1000,blank=True)    
    contact_no = models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=10,blank=True)
    photo_main = models.ImageField(default='default.png', upload_to='photos/%Y/%m/%d/',blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    is_published = models.BooleanField(default=True)
    tours_count = models. IntegerField(default=0)
    is_guide = models.BooleanField(default=False)
    price_per_hour= models.DecimalField(max_digits=5,default=0,decimal_places = 0)
    
    def __str__(self):
        return self.first_name

    def has_blogs(self):
        return True if self.email.blogs.all() else False

    def has_chat(self):
        chat = Chat.objects.filter(models.Q(sender=self.email) | models.Q(receiver=self.email))
        return True if chat else False

    def save(self):
        super().save()
        img = Image.open(self.photo_main.path)
        final_size=(400,400)
        width, height = img.size   # Get dimensions
        if width>400 or height >400:
            square_length = width if width<height else height
            left = (width - square_length)/2
            top = (height - square_length)/2
            right = (width + square_length)/2
            bottom = (height + square_length)/2
            img = img.crop((left, top, right, bottom))
            img.thumbnail(final_size)
            img.save(self.photo_main.path)
        
    


class Traveller_Review(models.Model):
    traveller = models.ForeignKey(Traveller, on_delete= models.CASCADE, related_name="review_of_traveller")
    traveller_reviewer = models.ForeignKey(Traveller, on_delete= models.CASCADE, related_name="traveller_reviewer")
    traveller_review = models.TextField(blank=True)
