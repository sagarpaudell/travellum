from django.db import models
from accounts.models import User
from places.models import Place
from travellers.models import Traveller
from datetime import datetime
from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='blog/photos/%Y/%m/%d/', blank=True)
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, related_name='blogs')
    is_guide = models.BooleanField(default=False, blank=False)
    like_users = models.ManyToManyField(User, related_name='likedblog', blank=True)
    post_time = models.DateTimeField(default=timezone.now , blank=True )

    def likes_count(self):
        return self.like_users.count()

    def __str__(self):
        return f'{self.id} by {self.user.email}'

    def blogger(self):
        return f'{self.user.first_name} {self.user.last_name}'

    def get_time(self):
        return self.post_time


class Comment(models.Model):
    blog_id=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='ofblog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    upvote_users = models.ManyToManyField(User, related_name='upvotedcomments')
    downvote_users = models.ManyToManyField(User, related_name='downvotedcomments')
    comment_time = models.DateTimeField(default=timezone.now , blank=True )

    def __str__(self):
        return f'{self.id} in {self.blog_id.pk}'

    def get_profile_pic(self):
        picture=Traveller.objects.get(email=self.user).photo_main
        return picture

    def commenter(self):
        return f'{self.user.first_name} {self.user.last_name}'
        
    def vote_count(self):
        return self.upvote_users.count() - self.downvote_users.count()


    

