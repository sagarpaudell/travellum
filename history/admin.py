from django.contrib import admin

from .models import History

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('id','traveller','guide','place')
    list_display_links = ('id', 'place')


admin.site.register(History, HistoryAdmin)
