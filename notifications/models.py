from django.db import models
from datetime import datetime
from accounts.models import User
from history.models import History
from django.utils import timezone
import math


class Notification(models.Model):
    receiver_email = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="receiver_email")
    sender_email = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="sender_email")
    sender_name = models.CharField(max_length=200,blank=True)
    title = models.CharField(max_length=200,blank=True)
    notification = models.TextField(blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    is_accepted = models.BooleanField(default=False)
    is_ignored = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)


    def __str__(self):
        return self.title


    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.reg_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "         print(traveller_id)hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"


class Trip_Notification(models.Model):
    receiver_email = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="trip_receiver_email")
    sender_email = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="trip_sender_email")
    form = models.ForeignKey(History, on_delete=models.CASCADE)
    has_accepted = models.BooleanField(default=False)
    has_rejected = models.BooleanField(default=False)
    noti_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.receiver_email.email

    def whenpublished(self):
        now = timezone.now()
        
        diff= now - self.noti_date

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds= diff.seconds
            
            if seconds == 1:
                return str(seconds) +  "second ago"
            
            else:
                return str(seconds) + " seconds ago"

            

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes= math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + " minute ago"
            
            else:
                return str(minutes) + " minutes ago"



        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours= math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "         print(traveller_id)hour ago"

            else:
                return str(hours) + " hours ago"

        # 1 day to 30 days
        if diff.days >= 1 and diff.days < 30:
            days= diff.days
        
            if days == 1:
                return str(days) + " day ago"

            else:
                return str(days) + " days ago"

        if diff.days >= 30 and diff.days < 365:
            months= math.floor(diff.days/30)
            

            if months == 1:
                return str(months) + " month ago"

            else:
                return str(months) + " months ago"


        if diff.days >= 365:
            years= math.floor(diff.days/365)

            if years == 1:
                return str(years) + " year ago"

            else:
                return str(years) + " years ago"

