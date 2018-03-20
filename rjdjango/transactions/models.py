from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    date = models.DateTimeField(auto_now_add=True)
    transType = models.CharField(max_length=120)
    sender = models.CharField(max_length=120)
    receiver = models.CharField(max_length=120)
    amount = models.IntegerField()
    senderAdd = models.CharField(max_length=120, blank=True, null=True)
    receiverAdd = models.CharField(max_length=120, blank=True, null=True)
    transID = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.title
