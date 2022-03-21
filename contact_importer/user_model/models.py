
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
# from django.core import validators
# from django.utils import timezone
# from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, AbstractUser
# from django.conf import settings
from django.contrib.auth import get_user_model
# import re


# Create your models here.

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, username, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email=email, username=username, password=password, **extra_fields)



class CustomUser(AbstractUser):
    username = models.CharField(_('username'), unique=True, max_length=20)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email



User = get_user_model()











# User = get_user_model()

# class UserManager(BaseUserManager):
#     def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
#         now = timezone.now()
#         if not username:
#             raise ValueError(_('The username must be filled'))
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email,
#                         is_staff=is_staff, is_active=True,is_superuser=is_superuser,
#                         last_login=now, date_joined=now, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_user(self, username, email=None, password=None, **extra_fields):
#         return self._create_user(username, email, password, False, False, **extra_fields)

#     def create_superuser(self, username, email, password, **extra_fields):
#         user=self._create_user(username, email, password, True, True,**extra_fields)
#         user.is_active=True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser, PermissionsMixin):
#     # username = models.CharField(_('username'), max_length=15, unique=True,
#     #                             help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
#     #                             validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),_('Enter a valid username.'),_('invalid'))])
#     # first_name = models.CharField(_('first name'), max_length=30)
#     # last_name = models.CharField(_('last name'), max_length=30)
#     email = models.EmailField(_('email address'), max_length=255, unique=True)
#     is_staff = models.BooleanField(_('staff status'), default=False, 
#                                 help_text=_('Designates whether the user can log into this admin site.'))
#     is_active = models.BooleanField(_('active'), default=True,
#                                 help_text=_('Designates whether this user should be treated as active. \
#                                 Unselect this instead of deleting accounts.'))
#     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#     # is_trusty = models.BooleanField(_('trusty'), default=False,
#     #                             help_text=_('Designates whether this user has confirmed his account.'))

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']  # , 'first_name', 'last_name']
    
#     objects = UserManager()

#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
    
#     # def get_full_name(self):
#     #     full_name = '%s %s' % (self.first_name, self.last_name)
#     #     return full_name.strip()
    
#     # def get_short_name(self):
#     #     return self.first_name
    
#     # def email_user(self, subject, message, from_email=None):
#     #     send_mail(subject, message, from_email, [self.email])