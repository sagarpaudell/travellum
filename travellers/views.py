from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User
from travellers.models import Traveller, Traveller_Review
from places.models import Place
from history.models import History
from guides.models import Guide, Guide_Review
from notifications.models import Notification, Trip_Notification
from history.models import History
from django.contrib import messages,auth
from datetime import datetime
import datetime
from django.utils.timezone import utc
import decimal

def view_profile(request, traveller_id):
    user=request.user
    if user.is_authenticated:
        notifications = Notification.objects.all().filter(receiver_email=user).order_by('-reg_date')
        traveller_user_logged_in = get_object_or_404(Traveller, email=user)
        if traveller_user_logged_in.is_guide:
            guide_user = get_object_or_404(Guide, email=user)
            if guide_user:
                trip_notifications = Trip_Notification.objects.all().filter(sender_email=user).order_by('-noti_date')
        
        else:
            trip_notifications = Trip_Notification.objects.all().filter(receiver_email=user).order_by('-noti_date')
    profile=get_object_or_404(Traveller, pk=traveller_id)
    bio = profile.bio.split('.',5)
    bio_first = ". ".join(bio[:5])+(".")
    guide_reviews = Guide_Review.objects.all().filter(guide=profile.email)
    guide_review_exists = False
    for guide_review in guide_reviews:
        if (guide_review.guide_reviewer.email==user):
            guide_review_exists=True
    traveller_reviews = Traveller_Review.objects.all().filter(traveller=profile)
    traveller_review_exists = False
    for traveller_review in traveller_reviews:
        if (traveller_review.traveller_reviewer.email==user):
            traveller_review_exists=True
    guide = Guide.objects.filter(email=profile.email).first()
    guide_historys = History.objects.all().filter(guide=profile.email,tour_complete=True)
    traveller_historys = History.objects.all().filter(traveller=profile.email,tour_complete=True)
    if 'guide_review' in request.POST:
        guide_rating =  request.POST.get('rating')
        guide_review = request.POST['review']
        guide = get_object_or_404(User, email=profile.email)
        guide_user = get_object_or_404(Guide, email=profile.email)
        guide_reviewer = traveller_user_logged_in
        g_review = Guide_Review(guide = guide, guide_reviewer=guide_reviewer, guide_review=guide_review, guide_ratings=guide_rating)
        g_review.save()
        guide_user.average_rating = ((float(guide_user.average_rating)*guide_reviews.count())+(float(guide_rating)))/(float(guide_reviews.count()+1))
        guide_user.save()
        return redirect ('/view_profile/'+str(traveller_id))

    if 'edit_guide_review' in request.POST:
        guide_review_id=request.POST['guide_review_id']
        eg_review = get_object_or_404(Guide_Review, pk=guide_review_id)
        old_rating = eg_review.guide_ratings
        eg_review.guide_review = request.POST['new_guide_review']
        eg_review.guide_ratings = request.POST['new_rating']
        eg_review.save()
        guide_user = get_object_or_404(Guide, email=profile.email)
        guide_user.average_rating = ((float(guide_user.average_rating)*(guide_reviews.count())+float(eg_review.guide_ratings)-float(old_rating)))/float(guide_reviews.count())
        guide_user.save()
        return redirect ('/view_profile/'+str(traveller_id))

    if 'delete_guide_review' in request.POST:
        guide_review_id=request.POST['guide_review_id']
        dg_review = get_object_or_404(Guide_Review, pk=guide_review_id)
        old_rating = dg_review.guide_ratings
        dg_review.delete()
        guide_user = get_object_or_404(Guide, email=profile.email)
        guide_user.average_rating = ((float(guide_user.average_rating)*guide_reviews.count())-float(old_rating))/(guide_reviews.count()-1)
        guide_user.save()
        return redirect ('/view_profile/'+str(traveller_id))

    if 'traveller_review' in request.POST:
        traveller_review = request.POST['tra_review']
        traveller = get_object_or_404(Traveller, email=profile.email)
        traveller_reviewer = traveller_user_logged_in
        t_review = Traveller_Review(traveller = traveller, traveller_reviewer=traveller_reviewer, traveller_review=traveller_review)
        t_review.save()
        return redirect ('/view_profile/'+str(traveller_id))

    if 'edit_traveller_review' in request.POST:
        traveller_review_id=request.POST['traveller_review_id']
        et_review = get_object_or_404(Traveller_Review, pk=traveller_review_id)
        et_review.traveller_review = request.POST['new_traveller_review']
        et_review.save()
        return redirect ('/view_profile/'+str(traveller_id))

    if 'delete_traveller_review' in request.POST:
        traveller_review_id=request.POST['traveller_review_id']
        dt_review = get_object_or_404(Traveller_Review, pk=traveller_review_id)
        dt_review.delete()
        return redirect ('/view_profile/'+str(traveller_id))

    if profile.email==user:
        return redirect('dashboard')

    elif user.is_authenticated:
        guide_travel_history = History.objects.all().filter(traveller = user , guide = profile.email)
        guide_has_travelled_with = False
        if guide_travel_history:
            for history in guide_travel_history:
                if history.tour_complete:
                    guide_has_travelled_with = True
        traveller_travel_history = History.objects.all().filter(traveller = profile.email , guide = user)
        traveller_has_travelled_with = False
        if traveller_travel_history:
            for history in traveller_travel_history:
                if history.tour_complete:
                    traveller_has_travelled_with = True
        notification_history = Notification.objects.all().filter(receiver_email = profile.email , sender_email = user).order_by('-reg_date')
        trip_notifications = Trip_Notification.objects.all().filter(receiver_email=user).order_by('-noti_date')

        
        if notifications:
            new_noti = notifications.last().reg_date
            if notifications.count()>1:
                last_noti = notifications[1].reg_date
                new_noti_check = (last_noti<new_noti)
                if (new_noti_check):
                    messages.info(request, 'You have new notifications.')
                else:
                    messages.info(request, 'You have no new notifications')
        if trip_notifications:
            new_tnoti = trip_notifications.last().noti_date
            if trip_notifications.count()>1:
                last_noti = trip_notifications[1].noti_date
                new_noti_check = (last_noti<new_noti)
                if (new_noti_check):
                    messages.info(request, 'You have new notifications.')
                else:
                    messages.info(request, 'You have no new notifications')
            elif trip_notifications.count()==1:
                messages.info(request, 'You have new notifications.')

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
                'guide_has_travelled_with': guide_has_travelled_with,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
                'has_accepted': has_accepted,
                'guide':guide,
                'guide_historys': guide_historys,
                'traveller_historys': traveller_historys,
                'guide_review_exists':guide_review_exists,
                'traveller_reviews': traveller_reviews,
                'traveller_review_exists': traveller_review_exists,
                'traveller_has_travelled_with': traveller_has_travelled_with,
                 }

        if (len(bio)>=5):
            bio_second = bio[5]
            context = {
                'logged_in_user':traveller_user_logged_in,     #logged_in_user is for avatar in navbar
                'traveller_user':profile,
                'my_profile':False,
                'notifications': notifications,
                'trip_notifications': trip_notifications,
                'guide_has_travelled_with': guide_has_travelled_with,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
                'bio_second': bio_second,
                'has_accepted':has_accepted,
                'guide':guide,
                'guide_historys': guide_historys,
                'traveller_historys': traveller_historys,
                'guide_review_exists':guide_review_exists,
                'traveller_reviews': traveller_reviews,
                'traveller_review_exists': traveller_review_exists,
                'traveller_has_travelled_with': traveller_has_travelled_with,
            }
        return render(request, 'travellers/travellers.html',context)

    else:
        context = {
                'traveller_user':profile,
                'my_profile':False,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
                'guide':guide,
                'guide_historys': guide_historys,
                'traveller_historys': traveller_historys,
                'guide_review_exists':guide_review_exists,
                'traveller_reviews': traveller_reviews,
                'traveller_review_exists': traveller_review_exists,
            }
        
        if (len(bio)>=5):
            bio_second = bio[5]
            context = {
                'traveller_user':profile,
                'my_profile':False,
                'guide_reviews': guide_reviews,
                'bio_first': bio_first,
                'bio_second': bio_second,
                'guide':guide,
                'guide_historys': guide_historys,
                'traveller_historys': traveller_historys,
                'guide_review_exists':guide_review_exists,
                'traveller_reviews': traveller_reviews,
                'traveller_review_exists': traveller_review_exists,
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
    guide_user = get_object_or_404(Guide , email=request.user)
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
       nop = float(no_of_people)
       noc = float(no_of_children)
       noh = float(total_hours)
       if ((nop+noc*0.75)<=2):
           tp=2*noh*float(guide_user.price)
           tp=int(tp)
       else:
           tp=(nop+noc*0.75)*noh*float(guide_user.price)
           tp=int(tp)
       history= History(traveller=traveller, guide=guide, place=place, no_of_people=no_of_people, no_of_children=no_of_children, total_hours=total_hours, total_price=tp)
       history.save()
       trip_notification=Trip_Notification(receiver_email=traveller_user.email, sender_email = request.user, form= history)
       trip_notification.save()
       traveller_id = request.POST['traveller_id']
       return redirect('/view_profile/'+traveller_id)
    guide_user = guide_user.places.all().first()
    context = {
                'traveller_user':traveller_user,
                'logged_in_user':traveller_user_logged_in,
                'places':places,
                'place_pattern':place_pattern[:-1],
                'guide_user':guide_user,
            }
    # print(guide_user.place)
    return render(request, 'travellers/create_trip.html',context)


