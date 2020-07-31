from django.contrib import admin

from .models import Traveller

class TravellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','address','is_guide')
    list_display_links = ('id', 'email')
    list_filter = ('city','country' )


admin.site.register(Traveller, TravellerAdmin)
