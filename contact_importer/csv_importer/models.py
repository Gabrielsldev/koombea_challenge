from pickle import TRUE
from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    date_of_birth = models.DateField(blank=False, null=True)
    phone = models.CharField(max_length=30, blank=False, null=True)
    address = models.CharField(max_length=255, blank=False, null=True)
    credit_card = models.CharField(max_length=20, blank=False, null=False)
    franchise = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=True)
    on_hold = models.BooleanField(default=False)
    processing = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

class csvFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='csvfiles/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

