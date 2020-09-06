from accounts.models import User
from chat.models import Chat
from travellers.models import Traveller

from operator import itemgetter

from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def chat(request, email):
    friend_user=User.objects.filter(email=email).first()
    friend_userid=friend_user.id              #the one the peson is chatting with
    current_user=request.user     #logged in user 
    index=0
    user_name_chat=[]               
    
    all_chat_list = Chat.objects.filter(Q(sender=current_user) | Q(receiver=current_user))  #every chat of the logged in user
    chat_list = Chat.objects.filter(Q(sender=current_user,receiver=friend_userid) | Q(receiver=current_user,sender=friend_userid)) #user specific chat list
    
    #save message to database
    if request.method == 'POST':
        hello = Chat(sender=request.user, receiver=User.objects.get(id=friend_userid), message_text=request.POST['message'])
        hello.save()
    
    for chat in all_chat_list:
        user = chat.receiver if chat.sender==current_user else chat.sender
        if any(user == x['user'] for x in user_name_chat):    
            continue
        else:
            messages= all_chat_list.filter(Q(sender=user) | Q(receiver=user)).last()
            last_message_time=messages.message_time.isoformat()
            is_last_messagebycurrentuser= True if messages.sender==current_user else False
            photo=Traveller.objects.filter(email=user).first().photo_main  
            print(photo) 
            user_name_chat.append({
                'user':user, 
                'messages' : messages, 
                'last_message' : messages.message_text[:40],
                'is_last_messagebycurrentuser' : is_last_messagebycurrentuser, 
                'user_photo' : photo, 
                'last_message_time' : last_message_time
            })        
           
        # print(index)
        # print(user_name_chat[0]['is_last_messagebycurrentuser'])
        # print(user_name_chat[index]['user'])
        # print(user_name_chat[index]['last_message'])
        # print(chat_list)
        
        index+=1
    
    user_name_chat=sorted(user_name_chat, key=itemgetter('last_message_time'), reverse=True)
        
    context={ 
        'chat_details':user_name_chat,
        'chat_friend':User.objects.get(id=friend_userid) ,
        'chat_list':chat_list,
        'traveller_currentuser':Traveller.objects.filter(email=current_user.id).first(),
        'traveller_chatuser':Traveller.objects.filter(email=friend_user.id).first()
        
    }
    
    print(context['traveller_currentuser'].photo_main)
   
    

    return render(request, "chat/chat.html", context)
@login_required
def chatRedirect(request):
    chat_list = Chat.objects.filter(Q(sender=request.user) | Q(receiver=request.user))
    try:
        chat = chat_list[0]
        user = chat.receiver if chat.sender==request.user else chat.sender
        print(user.email)
        return redirect(f"{user.email}")

    except:
        print(chat_list.first())
        #print(user.email)
        return redirect("index")
   


@login_required
def course_chat_room(request, course_id):
    print(course_id)
    return render(request, 'chat/room.html', {'course_id': course_id})
    