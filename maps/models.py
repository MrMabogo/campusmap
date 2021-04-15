from django.db import models
from django.contrib.auth.models import User

class SavedRoute(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    routeNumber = models.IntegerField(default=0)
    coordinates = models.JSONField(default=dict)