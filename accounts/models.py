from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False, is_sponser=False, is_organizer=False):
        # """
        # Creates and saves a User with the given email and password.
        # """
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have password')
        # if not name:
        #     raise ValueError('Users must have a name')
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        # user = self.model(
        #     email=self.normalize_email(email),
        # )

        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
       
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        # """
        # Creates and saves a staff user with the given email and password.
        # """
        user = self.create_user(
            email,
            password=password,
            is_staff =True

        )
        # user.staff = True
        # user.save(using=self._db)
        return user

  

    def create_superuser(self, email, password=None):
        # """
        # Creates and saves a superuser with the given email and password.
        # """
        user = self.create_user(
            email,
            password=password,
            is_staff = True,
            is_admin = True
        )
        # user.staff = True
        # user.admin = True
        # user.save(using=self._db)
        return user

    # def get_by_natural_key(self, email_):
    #     return self.get(code_number=email_)

class User(AbstractBaseUser):
    email = models.EmailField(
        # verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # name = models.CharField(max_length=255,
    #     )

    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    
    # notice the absence of a "Password field", that is built in.
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    objects = UserManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def natural_key(self):
        return self.email

    def has_perm(self, perm, ob=None):
        return True
        
    def has_module_perms(self, app_label):
        return True

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    @property
    def is_staff(self):
        # "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        # "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        # "Is the user active?"
        return self.active

  

# class user_type(models.Model):
#     is_sponser = models.BooleanField(default=False)
#     is_organizer = models.BooleanField(default=False)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         if self.is_sponser == True:
#             return User.get_email(self.user) + " - is_sponser"
#         else:
#             return User.get_email(self.user) + " - is_organizer"


    