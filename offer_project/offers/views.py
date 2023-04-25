from django.shortcuts import render
from offers.models import Offer, Category
# Create your views here.
def main(request):
    offers = Offer.objects.all()
    context ={
        "offers": offers
    }
    return render(request, 'offers/main.html', context)