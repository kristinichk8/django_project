from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from account.forms import UserLoginForm, UserRegistrationForm

# def account(request):
#     return render(request, './mainApp/login.html')
# Create your views here.



def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context={
        'form': form,
        'title': 'Login'
    }
    return render(request, './mainApp/login.html', context)


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляем! Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('account:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form,
        'title': 'Registration'
    }
    return render(request, './mainApp/register.html', context)