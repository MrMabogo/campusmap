from django.db import models
from django.contrib.auth.models import User

class MapUser(User):
    pass

class SavedRoute(models.Model):
    owner = models.ForeignKey(MapUser, on_delete=models.CASCADE)
    coordinates = models.JSONField()