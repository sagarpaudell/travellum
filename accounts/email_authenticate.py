from itsdangerous import URLSafeTimedSerializer as Serializer


from django.core.mail import send_mail
x='email@gmail.com'
s= Serializer('this is a secret')
def send_email(email,request):
    global x
    x=email
    message = s.dumps(email)
    full_url = request.build_absolute_uri()
    send_mail(
        'Email confirmation',
        f'Thank you for registering in travellum\n \
        here is your confirmation mail \n \
        {full_url[0:-9]}profile/{message}',
        'buddhagautam231@gmail.com',
        [email],
        fail_silently=False,
    )

def check_token(slug):
   
    print(slug)
    try:
        data=s.loads(slug, max_age=600)
    except:
        return False
    if data==x: 
        return True
    else: 
        return False
       