from django.contrib import admin
from .models import Blog, Comment

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'post_time',)
    list_display_links = ('id','title', 'user')
    list_filter = ('user', 'post_time',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    list_display_links = ('id','user' )
    list_filter = ('user', 'blog_id', 'comment_time')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
