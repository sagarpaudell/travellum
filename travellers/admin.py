from django.contrib import admin

from .models import Traveller,Traveller_Review

class TravellerAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','email','address','is_guide',)
    list_display_links = ('id', 'email')
    list_filter = ('city','country' )


admin.site.register(Traveller, TravellerAdmin)

class Traveller_ReviewAdmin(admin.ModelAdmin):
    list_display = ('traveller','traveller_reviewer')
    list_display_links = ('traveller','traveller_reviewer')

admin.site.register(Traveller_Review, Traveller_ReviewAdmin)

