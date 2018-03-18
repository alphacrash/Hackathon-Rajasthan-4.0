from django.shortcuts import render
from django.views.generic import ListView
from .models import Estate


class Profile(ListView):
    template_name = 'profile.html'

    def get_queryset(self):
        return Estate.objects.all()
