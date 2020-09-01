from django.db import models
from datetime import datetime
from accounts.models import User

class Notification(models.Model):
    receiver_email = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="receiver_email")
    sender_email = models.ForeignKey(User, on_delete= models.DO_NOTHING, blank=True, related_name="sender_email")
    sender_name = models.CharField(max_length=200,blank=True)
    title = models.CharField(max_length=200,blank=True)
    notification = models.TextField(blank=True)
    reg_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title
