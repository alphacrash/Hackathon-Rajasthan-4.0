from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', context=None)
    else:
        return HttpResponseRedirect('/accounts/login/')


def index(request):
    return render(request, "index.html", context=None)


def profile(request):
    return render(request, "profilepage.html", context=None)


def successful(request):
    return render(request, "successful.html", context=None)
