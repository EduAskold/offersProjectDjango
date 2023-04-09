from django.db import models
from company.models import Company
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
class Offer(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    skills = models.TextField(null=True, blank=True)
    create_date = models.DateField(auto_now=True)
    creator = models.ForeignKey(Company, on_delete=models.CASCADE)
    type_job = models.CharField(max_length=255)
    location = models.CharField(max_length=255)