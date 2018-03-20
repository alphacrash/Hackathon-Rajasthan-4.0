from django import forms
from transactions.models import Transaction


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'title',
            'transType',
            'sender',
            'receiver',
            'amount',
        ]
