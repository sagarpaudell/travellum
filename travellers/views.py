from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from travellers.models import Traveller
from places.models import Place
from history.models import History
from guides.models import Guide, Guide_Review
from notifications.models import Notification, Trip_Notification
from history.models import History
from django.contrib import messages,auth
from datetime import datetime
import datetime
from django.utils.timezone import utc

def view_profile(request, traveller_id):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user)
        traveller_user_logged_in = get_object_or_404(Traveller, email=user)
    if traveller_user_logged_in.is_guide:
        guide_user = get_object_or_404(Guide, email=user)
        if guide_user:
            trip_notifications = Trip_Notification.objects.all().filter(sender_email=user)
        
    else:
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=user)
    profile=get_object_or_404(Traveller, pk=traveller_id)
    bio = profile.bio.split('.',5)
    bio_first = ". ".join(bio[:5])+(".")
    guide_reviews = Guide_Review.objects.all().filter(guide=profile.email)
    if request.method == 'POST':
        guide_rating =  request.POST.get('rating')
        guide_review = request.POST['review']
        guide = get_object_or_404(User, email=profile.email)
        guide_reviewer = traveller_user_logged_in
        g_review = Guide_Review(guide = guide, guide_reviewer=guide_reviewer, guide_review=guide_review, guide_ratings=guide_rating)
        g_review.save()
    if profile.email==user:
        return redirect('dashboard')

    elif user.is_authenticated:
        travel_history = History.objects.all().filter(traveller = user , guide = profile.email)
        has_travelled_with = False
        if travel_history:
            for history in travel_history:
                if history.tour_complete:
                    has_travelled_with = True
        notification_history = Notification.objects.all().filter(receiver_email = profile.email , sender_email = user)
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=user)
        has_accepted = False
        for noti in notification_history:
            if noti.is_accepted:
                has_accepted = True
        context = {
                'logged_in_user':traveller_user_logged_in,     #logged_in_user is for avatar in navbar
                'traveller_user':profile,
                'my_profile':False,
                'notifications': notifications,
                'trip_notifications': trip_notifications,
                'has_travelled_with': has_travelled_with,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
                'has_accepted': has_accepted,
                 }

        if (len(bio)>=5):
            bio_second = bio[5]
            context = {
                'logged_in_user':traveller_user_logged_in,     #logged_in_user is for avatar in navbar
                'traveller_user':profile,
                'my_profile':False,
                'notifications': notifications,
                'trip_notifications': trip_notifications,
                'has_travelled_with': has_travelled_with,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
                'bio_second': bio_second,
                'has_accepted':has_accepted,
            }
        return render(request, 'travellers/travellers.html',context)

    else:
        context = {
                'traveller_user':profile,
                'my_profile':False,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
            }
        
        if (len(bio)>=5):
            bio_second = bio[5]
            context = {
                'traveller_user':profile,
                'my_profile':False,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
                'bio_second': bio_second,
            }
        return render(request, 'travellers/travellers.html',context)




def notifications(request):
    if request.method == 'POST':
        sender_user = request.user
        traveller_id = request.POST['traveller_id']

        receiver = get_object_or_404(Traveller, pk=traveller_id)
        sender_name = sender_user.first_name+" " +sender_user.last_name
        receiver_user = get_object_or_404(User, email=receiver.email)
        reg_date = datetime.datetime.utcnow().replace(tzinfo=utc)

    #Check if user has made request already
    if request.user.is_authenticated:
        current_user = request.user
        has_requested = Notification.objects.all().filter(receiver_email=receiver_user, sender_email=sender_user, completed=False )
        
        if has_requested:
            messages.error(request, 'You have already made a request to this guide')
            return redirect('/view_profile/'+traveller_id)
        else:
            notification = Notification(receiver_email=receiver_user, sender_email=sender_user, sender_name = sender_name, reg_date= reg_date)
            notification.save()
        return redirect('/view_profile/'+traveller_id)        
    return redirect('/view_profile/'+traveller_id)

def create_trip(request, traveller_id):
    traveller_user = get_object_or_404 (Traveller , pk = traveller_id)
    traveller_user_logged_in = get_object_or_404(Traveller, email=request.user)
    places=Place.objects.all()
    place_pattern=''
    for place in places:
        place_pattern = place.name+'|'+place_pattern
    if 'confirm' in request.POST:
       traveller = traveller_user.email
       guide =  request.user
       place = Place.objects.filter(name=request.POST['place']).first()
       no_of_people = request.POST['no_of_people']
       no_of_children = request.POST['no_of_children']
       total_hours = request.POST['travel_hours']
       total_price = request.POST['cost']

       history= History(traveller=traveller, guide=guide, place=place, no_of_people=no_of_people, no_of_children=no_of_children, total_hours=total_hours, total_price=total_price)
       history.save()
       trip_notification=Trip_Notification(receiver_email=traveller_user.email, sender_email = request.user, form= history)
       trip_notification.save()
       traveller_id = request.POST['traveller_id']
       return redirect('/view_profile/'+traveller_id)
    context = {
                'traveller_user':traveller_user,
                'logged_in_user':traveller_user_logged_in,
                'places':places,
                'place_pattern':place_pattern[:-1],
            }
    return render(request, 'travellers/create_trip.html',context)


