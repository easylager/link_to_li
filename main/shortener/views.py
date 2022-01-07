from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, DomainForm
from .forms import UserRegistrationForm
from .models import Domain


HOST = 'http://127.0.0.1:8000/'


def home(request):
    return render(request, 'shortener/base.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
        return render(request, 'shortener/authorization.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'shortener/registration_done.html', context={'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'shortener/registration.html', context={'user_form': user_form})


def transform_domain(request):
    if request.method == 'POST':
       domain_form = DomainForm(request.POST)
       if domain_form.is_valid():
           new_domain = domain_form.save(commit=False)
           new_domain.user = request.user
           new_domain.save()
       return render(request, 'shortener/domain_form.html',
                     context={'form': domain_form, 'short_domain': new_domain.short_link}, )
    else:
        domain_form = DomainForm()
    return render(request, 'shortener/domain_form.html', context={'form': domain_form})


def redirect_to_origin(request, slug):
    domain = Domain.objects.get(short_link=HOST + slug)
    link = domain.link
    return render(request, 'shortener/redirect.html', context={'link': link})


def my_links(request):
    links = Domain.objects.filter(user=request.user)
    return render(request, 'shortener/my_links.html', context={'links': links})

