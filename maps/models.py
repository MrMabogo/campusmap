from django.db import models
from django.contrib.auth.models import User

class SavedRoute(models.Model):
    class Meta:
        unique_together = ('owner', 'name')

    name = models.CharField(max_length=100, default='')
    coordinates = models.JSONField(default=dict)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)