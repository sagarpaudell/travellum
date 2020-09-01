from django.contrib import admin

from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','receiver_email','sender_name','title')
    list_display_links = ('id', 'receiver_email','title')


admin.site.register(Notification, NotificationAdmin)
