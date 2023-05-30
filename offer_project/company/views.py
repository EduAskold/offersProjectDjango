from django.shortcuts import render
from offers.models import Offer
from company.models import Company
# Create your views here.
def company(request, id):
    company = Company.objects.get(id=id)
    offers = Offer.objects.filter(creator=company)
    context ={
        "offers": offers,
        "company": company
    }
    return render(request, 'company/company.html', context)