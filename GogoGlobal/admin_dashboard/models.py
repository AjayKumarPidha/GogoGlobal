import email
from email.mime import image
from operator import truediv
from pickle import TRUE
import uuid
import random
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.shortcuts import render
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_user(self, email_id, first_name, last_name, phone_number, password, choose_profilepic, gender, Country, address,  state,  city, Postal_zipcode):

        if not email_id:
            raise ValueError('The Email must be Set')
        if not first_name:
            raise ValueError("User Must have a first name")

        if not last_name:
            raise ValueError("User Must have a last name")
        fixed_digits = 5

        affiliate_id = random.randrange(00000, 99999, fixed_digits)

        user = self.model(
            email_id=self.normalize_email(email_id),
            first_name=first_name,
            last_name=last_name,
            choose_profilepic=choose_profilepic,
            phone_number=phone_number,
            gender=gender,
            Country=Country,
            address=address,
            state=state,
            city=city,
            Postal_zipcode=Postal_zipcode,
            affiliate_id=affiliate_id,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_id, first_name, last_name, phone_number, choose_profilepic, gender, Country, address, state, city, Postal_zipcode, password):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """

        Affiliate_id = models.CharField(null=True, blank=True, max_length=4)
        user = self.create_user(
            email_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            choose_profilepic=choose_profilepic,
            gender=gender,
            Country=Country,
            address=address,
            state=state,
            city=city,
            Postal_zipcode=Postal_zipcode,
            password=password,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

# Custom User Model ###########-
class CustomUser(AbstractBaseUser):
    user_id = models.CharField(
        max_length=250004, unique=True, null=True, blank=True)
    is_vendor = models.BooleanField(default=True)
    is_affiliator = models.BooleanField(default=False)
    email_id = models.EmailField(verbose_name='email_id', max_length=255, unique=True, null=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    choose_profilepic = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    Country = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    Postal_zipcode = models.IntegerField(null=True, blank=True)
    affiliate_id = models.CharField(null=True, blank=True, max_length=4)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email_id'
    EMAIL_FIELD = 'email_id'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'choose_profilepic',
                       'gender', 'Country', 'address', 'state', 'city',  'Postal_zipcode']

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


def set_user_id(sender, instance, **kwargs):
    if not instance.user_id:
        user_id = ""
        counter = 1
        while CustomUser.objects.filter(user_id=user_id):
            user_id = "" + str(counter)
            counter += 1
            instance.user_id = user_id


models.signals.pre_save.connect(set_user_id, sender=CustomUser)


class HomePageBannerModel(models.Model):
    up_to_off = models.CharField(max_length=100, null=True, blank=True)
    headings = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


class PrivacyPolicyModel(models.Model):
    heading = models. CharField(max_length=1000, null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)


class TermsConditionsModel(models.Model):
    heading = models. CharField(max_length=1000, null=True, blank=True)
    descriptions = models.TextField(null=True, blank=True)
