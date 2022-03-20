from pickle import TRUE
from django.db import models

from django.contrib.auth import get_user_model

from django_cryptography.fields import encrypt

User = get_user_model()


# Create your models here.


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)

    name = models.CharField(max_length=255, blank=False, null=True)
    date_of_birth = models.DateField(blank=False, null=True)
    phone = models.CharField(max_length=30, blank=False, null=True)
    address = models.CharField(max_length=255, blank=False, null=True)
    credit_card = encrypt(models.CharField(max_length=20, blank=False, null=True))
    last_four_card_numbers = models.CharField(max_length=20, blank=False, null=True)
    franchise = models.CharField(max_length=20, blank=False, null=True)
    email = models.EmailField(blank=False, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']


class csvFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='csvfiles/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    on_hold = models.BooleanField(default=False)
    processing = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name