from django.contrib import admin

from .models import Place

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'city','country', 'is_published',)
    list_display_links = ('id',)
    list_filter = ('city','country' )


admin.site.register(Place, PlaceAdmin)
