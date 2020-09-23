from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Guide
from travellers.models import Traveller
from accounts.models import User
from history.models import History
from places.models import Place
# Create your views here.


def GuideView(request):
    user=request.user
    traveller_user=Traveller.objects.filter(email=user).first()
    
    traveller_user.is_guide = True
    traveller_user.save()
    docType = request.POST['docType']
    doc_photo_front= request.FILES['doc-front']
    doc_photo_back= request.FILES['doc-back']
    doc_number = request.POST['doc-number']
    
    
    if docType=="ctzn":
        guide_user = Guide(
        email=user, 
        citizenship_front=doc_photo_front, 
        citizenship_back=doc_photo_back,
        citizenship_number=doc_number,
        )
    else:
        guide_user = Guide(
        email=user, 
        driverlicense_front=doc_photo_front, 
        driverlicense_back=doc_photo_back,
        driverlicense_number=doc_number,
        )

    guide_user.save()
    guide_user=Guide.objects.filter(email=user).first()
    subject = f'{user.email} has requested to be published as guide'
    message = f'follow this link to publish the user \
        http://127.0.0.1:8000/admin/guides/guide/{guide_user.pk}/change'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['buddhagautam231@gmail.com', 'birajkmc4@gmail.com','s2a6m0@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    return redirect('dashboard')



def GuideUpdateView(request):
    user = User.objects.get(pk = request.user.pk)
    guide_user = Guide.objects.get(email = user)
    place = request.POST['place']
    guide_user.places.add(Place.objects.get(name=place))
    guide_user.price = request.POST['pph']
    guide_user.replies_within = request.POST['rep-with']
    guide_user.save()
    return redirect('dashboard')
        
    



