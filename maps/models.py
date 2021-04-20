from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class SavedRoute(models.Model):
    class Meta:
        unique_together = ('owner', 'name')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default='')
    coordinates = models.JSONField(default=dict)