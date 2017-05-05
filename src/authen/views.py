from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import requires_csrf_token
from django.contrib import messages

from .forms import LoginForm, RegistrationForm


# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, 'index.html')


@requires_csrf_token
def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/', status=200)
        else:
            form = LoginForm(request.POST)
            context = {'form': form}
            return render(request, 'login.html', context=context, status=401)
    if request.method == 'GET':
        form = LoginForm(None)
        context = {'form': form}
        return render(request, 'login.html', context=context)


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def auth_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
            return render(request, 'register.html', context=context)
        messages.success(request, 'Successfully registered. Please login now.')
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        form = RegistrationForm(None)
        context = {'form': form}
        return render(request, 'register.html', context=context)
