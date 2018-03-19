from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Transaction(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    transType = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    sender = models.CharField(max_length=120)
    senderAdd = models.CharField(max_length=120)
    receiver = models.CharField(max_length=120)
    receiverAdd = models.CharField(max_length=120)
    amount = models.IntegerField()
    transID = models.CharField(max_length=120)

    def __str__(self):
        return self.title
