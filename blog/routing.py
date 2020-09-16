from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/blog_detail/<id>', consumers.ChatConsumer),
]



