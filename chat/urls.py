from django.urls import path
from . import views as chatView

urlpatterns=[
    path('',chatView.chatRedirect, name='chat'),
    path('<str:email>',chatView.chat, name='chat_withemail'),
    # path('room/<int:course_id>/', chatView.course_chat_room, name='course_chat_room'),
]