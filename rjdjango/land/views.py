from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView

from land.models import Estate
from transactions.models import Transaction


class Profile(LoginRequiredMixin, ListView):
    template_name = 'land/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.filter(owner=self.request.user, transType__iexact='Land')
        context['transactions'] = transactions
        return context

    def get_queryset(self):
        return Estate.objects.filter(owner=self.request.user)
