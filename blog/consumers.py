import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from blog.models import Blog, Comment

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.blog_id = int(self.scope['url_route']['kwargs']['id'])
        self.user = self.scope['user']
        await self.accept()

    async def disconnect(self, text_data):
        pass

    async def receive(self, text_data):
        info = json.loads(text_data)
        print(info)
        count = await self.save_vote(info)
        info['count'] = count
        print(info)
        await self.send(text_data=json.dumps(info))   
        
    
    @database_sync_to_async
    def save_vote(self,info):
        if info['vote_type'] == 'like':
            blog_exist = Blog.objects.filter(like_users=self.user , id=self.blog_id)
            blog = Blog.objects.get(id=self.blog_id)
            if not blog_exist:
                blog.like_users.add(self.user)
                blog.save()
            else :
                blog.like_users.remove(self.user)

            return Blog.objects.get(id=self.blog_id).likes_count()
           
        
        if info['vote_type'] == 'upvote':
            comment_id = int(info['id'])
            comment=Comment.objects.get(id=comment_id)
            comment_exist_upvote = Comment.objects.filter(id=comment_id, upvote_users = self.user)
            comment_exist_downvote = Comment.objects.filter(id=comment_id, downvote_users = self.user)
            
            if comment_exist_upvote :
                comment.upvote_users.remove(self.user)
                comment.save()
            elif comment_exist_downvote :
                comment.downvote_users.remove(self.user)
                comment.save()
            else :
                comment.upvote_users.add(self.user)
                comment.save()

            comment=Comment.objects.get(id=comment_id)
            return comment.vote_count()

        if info['vote_type'] == 'downvote':
            comment_id = int(info['id'])
            comment=Comment.objects.get(id=comment_id)
            comment_exist_upvote = Comment.objects.filter(id=comment_id, upvote_users = self.user)
            comment_exist_downvote = Comment.objects.filter(id=comment_id, downvote_users = self.user)
            
            if comment_exist_downvote:
                comment.downvote_users.remove(self.user)
                comment.save()
            elif comment_exist_upvote :
                comment.upvote_users.remove(self.user)
                comment.save()
            else: 
                comment.downvote_users.add(self.user)

            comment=Comment.objects.get(id=int(info['id']))
            return comment.vote_count()
        

        
    
        # if info='upvote':
        #     comment = Comment.objects.get(id=)
        
    
    
            
    