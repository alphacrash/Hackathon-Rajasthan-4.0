from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class EMitra(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.title)
