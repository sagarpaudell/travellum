from django.db import models
from datetime import datetime
from accounts.models import User 

class Chat(models.Model):
    sender=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="sender")
    receiver=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="receiver")
    message_text=models.TextField(blank=True)
    message_time = models.DateTimeField(auto_now_add = True)