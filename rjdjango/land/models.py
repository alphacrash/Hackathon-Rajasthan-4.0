from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class Estate(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    own_id = models.CharField(max_length=120)
    plot = models.CharField(max_length=200)
    documents = models.CharField(max_length=50)
    area = models.TextField()
    tax = models.TextField()

    def __str__(self):
        return str(self.plot)
