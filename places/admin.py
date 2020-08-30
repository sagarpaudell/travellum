from django.contrib import admin

from .models import Place, Major_Attraction, Things_To_Do
from .models import Place, Review


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

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('Reviewer','place_name', 'ratings')
    list_display_links = ('Reviewer','place_name')
    list_filter = ('Reviewer','place_name' )

admin.site.register(Review, ReviewAdmin)
