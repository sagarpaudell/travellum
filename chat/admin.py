from django.contrib import admin
from chat.models import Chat

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver',  'message_text')
    # list_display_links = ('id', 'name')
   

admin.site.register(Chat,ChatAdmin)