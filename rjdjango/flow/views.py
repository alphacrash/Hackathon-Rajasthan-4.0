from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def home(request):
    if request.user.is_authenticated:
        return render(request, 'index.html', context=None)
    else:
        return HttpResponseRedirect('/accounts/login/')
