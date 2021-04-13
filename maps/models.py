from django.db import models
from django.contrib.auth.models import User

class SavedRoute(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    coordinates = models.JSONField()