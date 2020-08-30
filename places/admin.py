from django.contrib import admin

from .models import Place, Review


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'city','country', 'is_published',)
    list_display_links = ('id',)
    list_filter = ('city','country' )


admin.site.register(Place, PlaceAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('Reviewer','place_name', 'ratings')
    list_display_links = ('Reviewer','place_name')
    list_filter = ('Reviewer','place_name' )

admin.site.register(Review, ReviewAdmin)
