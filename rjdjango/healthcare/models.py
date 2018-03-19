from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Data(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    age = models.IntegerField()
    medical_history = models.TextField()
    immunization = models.TextField()
    allergies = models.TextField()
    hospital = models.TextField()
    insured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
