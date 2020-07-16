from django.contrib import admin

from .models import Traveller

class TravellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    list_display_links = ('id', 'name')
    list_filter = ('city','country' )


admin.site.register(Traveller, TravellerAdmin)
