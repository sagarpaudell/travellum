from django.contrib import admin

from .models import Notification, Trip_Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','receiver_email','sender_name','title', 'reg_date')
    list_display_links = ('id', 'receiver_email','title')
    list_filter = ['reg_date']
    
class Trip_NotificationAdmin(admin.ModelAdmin):
    list_display = ('id','receiver_email','sender_email')
    list_display_links = ('id', 'receiver_email','sender_email')

admin.site.register(Notification, NotificationAdmin)
admin.site.register(Trip_Notification, Trip_NotificationAdmin)

