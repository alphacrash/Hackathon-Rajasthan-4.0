from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from transactions.models import Transaction
from transactions.forms import TransactionForm


class List(LoginRequiredMixin, ListView):
    template_name = 'transactions.html'

    def get_queryset(self):
        return Transaction.objects.all()


class Profile(LoginRequiredMixin, ListView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        transactions = Transaction.objects.filter(owner=self.request.user)
        context['transactions'] = transactions
        return context

    def get_queryset(self):
        return Transaction.objects.filter(owner=self.request.user)


def order(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.owner = request.user
        instance.save()
        return HttpResponseRedirect('/')
    context = {
        'form': form,
    }
    return render(request, "order.html", context)
