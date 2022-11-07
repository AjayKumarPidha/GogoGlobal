from functools import total_ordering
from itertools import product
from operator import truediv
from django.db import models

# Create your models here.
from django.forms import CharField, ImageField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


########## Custom Model manager ########
class CustomUserManager(BaseUserManager):
    def create_user(self, email_id, first_name, last_name, phone_number, password, choose_profilepic):

        if not email_id:
            raise ValueError('The Email must be Set')
        if not first_name:
            raise ValueError("User Must have a first name")

        if not last_name:
            raise ValueError("User Must have a last name")

        user = self.model(
            email_id=self.normalize_email(email_id),
            first_name=first_name,
            last_name=last_name,
            choose_profilepic=choose_profilepic,
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email_id, first_name, last_name, phone_number, password, choose_profilepic):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email_id,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            choose_profilepic=choose_profilepic,
            password=password



        )
        user.set_password(password)
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

############ Custom User Model ###########


class CustomUser(AbstractBaseUser):
    email_id = models.EmailField(
        verbose_name='email_id', max_length=255, unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    choose_profilepic = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email_id'
    EMAIL_FIELD = 'email_id'
    REQUIRED_FIELDS = ['first_name', 'last_name',
                       'phone_number', 'choose_profilepic']

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


class ProductModel(models.Model):
    product_name = models.CharField(max_length=200, null=True, blank=True)
    product_description = models.TextField(null=True, blank=True)
    product_price = models.CharField(max_length=200, null=True, blank=True)
    product_quantity = models.CharField(max_length=200, null=True, blank=True)
    product_link = models.URLField(null=True, blank=True)
    product_image = models.FileField(null=True, blank=True)
    product_category = models.CharField(max_length=200, null=True, blank=True)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    vendor_id = models.IntegerField( null=True , blank=True)




class Manage_business(models.Model):
    business_name = models.CharField(max_length=200, null=True, blank=True)
    business_email_id = models.EmailField()
    business_phoneno = models.IntegerField(null=True, blank=True)
    business_paidtotal_earning = models.IntegerField(null=True, blank=True)
    business_unpaidtotal_earning = models.IntegerField(null=True, blank=True)
    unpaid_paid_referals = models.IntegerField(null=True, blank=True)
    paid_total_referals = models.IntegerField(null=True, blank=True)
