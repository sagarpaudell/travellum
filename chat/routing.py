from django.urls import path
from . import consumers


websocket_urlpatterns = [
    # re_path(r'ws/chat/(?P<email>\w+)/$', consumers.ChatConsumer),
    # re_path(r'ws/chat/bikesh@bimali.com/$', consumers.ChatConsumer),
    path('ws/chat/<email>/', consumers.ChatConsumer)
]


