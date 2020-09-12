from django.contrib import admin

from .models import Guide

class GuideAdmin(admin.ModelAdmin):
    list_display = ('id','email','is_published','tours_count')
    list_display_links = ('id','email', )
    # list_filter = ('city','country')


admin.site.register(Guide, GuideAdmin)


