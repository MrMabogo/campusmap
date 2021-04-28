from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.conf import settings

class SavedRoute(models.Model):
    class Meta:
        unique_together = ('owner', 'name')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default='')
    geojson = models.JSONField(default=dict)

class UVALocation(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    coordinates = models.JSONField(default=dict)
    properties = models.JSONField(default=dict)

class UVALocationCollection(models.Model):
    geojson = models.JSONField(default=dict)

class Recommendation(models.Model):
    location_idea = models.TextField()
    # post_date = models.DateField(auto_now_add=True)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
#     likes = models.ManyToManyField(User, related_name="recommendation")
    objects = models.Manager()

    def __str__(self):
        return self.location_idea

    def get_absolute_url(self):
        return reverse("maps:list")

