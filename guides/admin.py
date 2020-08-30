from django.contrib import admin

from .models import Guide, GuideReview

class GuideAdmin(admin.ModelAdmin):
    list_display = ('id','email','is_published','tours_count')
    list_display_links = ('id','email', )
    # list_filter = ('city','country')

class GuideReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer','guide','review_text','review_score')
    link_display_links=('reviewer','guide')

admin.site.register(Guide, GuideAdmin)
admin.site.register(GuideReview, GuideReviewAdmin)

