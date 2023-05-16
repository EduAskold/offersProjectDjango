from django.db import models
from offers.models import Offer
# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=255)
    surename = models.CharField(max_length=255)
    resume = models.FileField(upload_to="client/resume/", null=True, blank=True)
    image = models.ImageField(upload_to="client/image/", null=True, blank=True)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
class Aplication(models.Model):
    resume = models.FileField(upload_to="client/resume/")
    message = models.TextField(null=True, blank=True)
    create_date = models.DateField(auto_now=True)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)