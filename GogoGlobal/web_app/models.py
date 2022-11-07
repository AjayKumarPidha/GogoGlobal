import email
from operator import truediv
from django.db import models

# Create your models here.


class ContactEnquiryModels(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email_id = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    subject = models.CharField(max_length=400, null=True, blank=True)
    message = models.TextField(null=True, blank=True)