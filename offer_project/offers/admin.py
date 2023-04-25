from django.contrib import admin
from offers.models import Offer, Category
# Register your models here.
admin.site.register([Offer, Category])