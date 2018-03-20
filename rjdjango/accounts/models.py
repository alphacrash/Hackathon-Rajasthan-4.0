from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class UserAccount(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=120)

    def __str__(self):
        return self.username
