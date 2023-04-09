from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    count_workers = models.CharField(max_length=255)
    image = models.ImageField(upload_to="/company/", null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)