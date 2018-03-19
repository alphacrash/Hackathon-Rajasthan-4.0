from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from transactions.models import Transaction


class List(LoginRequiredMixin, ListView):
    template_name = 'transactions.html'

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)
