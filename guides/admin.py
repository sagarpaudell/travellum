from django.contrib import admin

from .models import Guide

class GuideAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'address')
    list_display_links = ('id', 'name')
    list_filter = ('city','country' )


admin.site.register(Guide, GuideAdmin)
