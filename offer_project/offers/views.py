from django.shortcuts import render, redirect
from offers.models import Offer, Category
from django.contrib.auth.models import User
from company.models import Company
from client.models import Client
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def main(request):
    offers = Offer.objects.all()
    context ={
        "offers": offers
    }
    return render(request, 'offers/main.html', context)
def offer(request, id):
    offer = Offer.objects.get(pk=id)
    context ={
        "offer": offer
    }
    return render(request, 'offers/offer.html', context)
def reg(request):
    context ={

    }
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == "0":
            company_name = request.POST.get('company_name')
            company_description = request.POST.get('company_description')
            company_count_workers = request.POST.get('company_count_workers')
            company_email = request.POST.get('company_email')
            company_password = request.POST.get('company_password')
            company_conf_password = request.POST.get('company_conf_password')
            if request.FILES['company_image']:
                company_image = request.FILES['company_image']
                fss = FileSystemStorage()
                file = fss.save(company_image.name, company_image)
                file_url = fss.url(file)
            if company_name and company_description and company_count_workers and company_email and company_password and company_conf_password:
                if len(company_password)>=8:
                    if company_password == company_conf_password:
                        try:
                            user = User.objects.create_user(username=company_email, password=company_password)
                            company = Company.objects.create(name = company_name, description = company_description, count_workers = company_count_workers, user = user, image = file_url)
                        except:
                            context['error'] = "Користувач з такою електронною поштою вже існує"
                    else:
                        context['error'] = "Паролі не співпадають"
                else:
                    context['error'] = "Довжина паролю меньша за 8 символів"
            else:
                context['error'] = "Заповніть всі поля"
        elif user_type == "1":
            context['form_type'] = "user"
            finder_name = request.POST.get('finder_name')
            finder_surename = request.POST.get('finder_surename')
            finder_email = request.POST.get('finder_email')
            finder_phone_number = request.POST.get('finder_phone_number')
            finder_password = request.POST.get('finder_password')
            finder_conf_password = request.POST.get('finder_conf_password')
            if request.FILES['finder_resume']:
                finder_resume = request.FILES['finder_resume']
                fss = FileSystemStorage()
                file = fss.save(finder_resume.name, finder_resume)
                file_resume_url = fss.url(file)
            if request.FILES['finder_image']:
                finder_image = request.FILES['finder_image']
                fss = FileSystemStorage()
                file = fss.save(finder_image.name, finder_image)
                file_image_url = fss.url(file)
            if finder_name and finder_surename and finder_email and finder_phone_number and finder_password and finder_conf_password:
                if len(finder_password)>=8:
                    if finder_password == finder_conf_password:
                        try:
                            user = User.objects.create_user(username=finder_email, password=finder_password)
                            client = Client.objects.create(name = finder_name, surename = finder_surename, email = finder_email, phone_number = finder_phone_number, resume = file_resume_url, image = file_image_url, user=user)
                        except:
                            context['error'] = "Користувач з такою електронною поштою вже існує"
                    else:
                        context['error'] = "Паролі не співпадають"
                else:
                    context['error'] = "Довжина паролю меньша за 8 символів"
            else:
                context['error'] = "Заповніть всі поля"
    return render(request, 'offers/reg.html', context)
def log(request):
    context ={

    }
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == "0":
            context['form_type'] = "company"
            company_log_email = request.POST.get('company_log_email')
            company_log_password = request.POST.get('company_log_password')
            user = authenticate(username = company_log_email, password = company_log_password)
            if user:
                try:
                    Company.objects.get(user = user)
                    login(request, user)
                    return redirect('main')
                except:
                    context['error'] = "Користувача/компанії з такою електронною поштою не існує"
            else:
                context['error'] = "Логін або пароль невірний"
        elif user_type == "1":
            context['form_type'] = "user"
            finder_log_email = request.POST.get('finder_log_email')
            finder_log_password = request.POST.get('finder_log_password')
            user = authenticate(username = finder_log_email, password = finder_log_password)
            if user:
                try:
                    Client.objects.get(user = user)
                    login(request, user)
                    return redirect('main')
                except:
                    context['error'] = "Користувача з такою електронною поштою не існує"
            else:
                context['error'] = "Логін або пароль невірний"
    return render(request, 'offers/log.html', context)