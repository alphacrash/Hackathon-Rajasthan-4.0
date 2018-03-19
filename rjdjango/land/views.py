from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from land.models import Estate


class Profile(LoginRequiredMixin, ListView):
    template_name = 'land/profile.html'

    def get_queryset(self):
        return Estate.objects.filter(owner=self.request.user)
