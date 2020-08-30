from django.contrib import admin

from .models import Place, Major_Attraction, Things_To_Do

class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'city','country', 'is_published',)
    list_display_links = ('id',)
    list_filter = ('city','country' )

class Major_Attraction_Admin(admin.ModelAdmin):
    list_display = ('id', 'place' , 'attraction_name',)
    list_display_links = ('id', 'attraction_name',)

class Things_To_Do_Admin(admin.ModelAdmin):
    list_display = ('id', 'place' , 'task_name',)
    list_display_links = ('id', 'task_name',)


admin.site.register(Place, PlaceAdmin)
admin.site.register(Major_Attraction, Major_Attraction_Admin)
admin.site.register(Things_To_Do, Things_To_Do_Admin)
