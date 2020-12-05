from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .models import MyUser


# Create your views here.

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=password)
            login(request, account)
            return redirect('profile')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form
        print(form)

    return render(request, 'account/register.html', context)


def login_view(request):
    context = {}
    if request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')
        account = authenticate(email=email, password=password)
        print(1)
        login(request, account)
        print('iam login')
        return redirect('profile')
    return render(request, 'account/login.html')

@login_required
def user_profile(request):
    profile = MyUser.objects.all()
    return render(request, 'account/profile.html', {'profile': profile})


def logout_view(request):
    logout(request)
    return HttpResponse('you are logout')
