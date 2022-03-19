from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    phone = models.CharField(max_length=30, blank=False, null=False)
    address = models.CharField(max_length=255, blank=False, null=False)
    credit_card = models.CharField(max_length=20, blank=False, null=False)
    franchise = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)

class csvFile(models.Model):
    name = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='csvfiles/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

