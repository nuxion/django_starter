from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
import hashlib
from allauth.socialaccount.models import SocialLogin
from django.core.handlers.wsgi import WSGIRequest

# from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # profile_pic = models.TextField(max_length=500, blank=True)
    username = None
    email = models.EmailField('email address', unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, primary_key=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=512, blank=True, null=True)
    first_name = models.CharField(max_length=512, blank=True, null=True)
    last_name = models.CharField(max_length=512, blank=True, null=True)
    locale = models.CharField(max_length=5, null=False, default="en")
    avatar_url = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return force_text(self.user.email)


@receiver(user_logged_in)
def social_login_extra(sender: CustomUser, request: WSGIRequest, *args, **kwargs):
    sociallogin: SocialLogin = kwargs.get('sociallogin')
    preferred_avatar_size_pixels = 256

    avatar_url = "http://www.gravatar.com/avatar/{0}?s={1}".format(
        hashlib.md5(request.user.email.encode('UTF-8')).hexdigest(),
        preferred_avatar_size_pixels
    )

    if sociallogin:
        # Extract first / last names from social nets and store on User record
        if sociallogin.account.provider == 'google':
            fullname = sociallogin.account.extra_data['name']
            first_name = sociallogin.account.extra_data['given_name']
            last_name = sociallogin.account.extra_data['family_name']
            avatar_url = sociallogin.account.extra_data.get('picture', avatar_url)

        if sociallogin.account.provider == 'github':
            fullname = sociallogin.account.extra_data['name']
            try:
                first_name = sociallogin.account.extra_data['name'].split()[0]
                last_name = sociallogin.account.extra_data['name'].split()[1]
            except IndexError:
                first_name = None
                last_name = None
            except AttributeError:
                first_name = None
                last_name = None
            avatar_url =  sociallogin.account.extra_data.get('avatar_url', avatar_url)

        obj, created = UserProfile.objects.get_or_create(
            user=request.user, fullname=fullname,
            first_name=first_name, last_name=last_name,
            avatar_url=avatar_url,
        )
        if obj.avatar_url != avatar_url:
            obj.avatar_url = avatar_url
            obj.save()
        # obj.save()
