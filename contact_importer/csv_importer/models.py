from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=True)
    phone = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    credit_card = models.CharField(max_length=20, blank=False, null=False)
    franchise = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    on_hold = models.BooleanField(default=False)
    processing = models.BooleanField(default=False)
    failed = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)

class csvFile(models.Model):
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='csvfiles/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

