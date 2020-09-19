from django.contrib import admin

from .models import Guide,Guide_Review

class GuideAdmin(admin.ModelAdmin):
    list_display = ('id','email','is_published','tours_count')
    list_display_links = ('id','email', )
    # list_filter = ('city','country')


admin.site.register(Guide, GuideAdmin)

class Guide_ReviewAdmin(admin.ModelAdmin):
    list_display = ('guide','guide_reviewer', 'guide_ratings')
    list_display_links = ('guide','guide_reviewer')

admin.site.register(Guide_Review, Guide_ReviewAdmin)


