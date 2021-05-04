from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from django.urls import reverse, reverse_lazy
from django.conf import settings
from django.utils import timezone

class SavedRoute(models.Model):
    class Meta:
        unique_together = ('owner', 'name')

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, default='')
    geojson = models.JSONField(default=dict)
    
    def __str__(self):
        return self.name

class UVALocation(models.Model):
    name = models.CharField(max_length=100, default='', unique=True)
    coordinates = models.JSONField(default=dict)
    properties = models.JSONField(default=dict)

    def __str__(self):
        return self.name

class UVALocationCollection(models.Model):
    geojson = models.JSONField(default=dict)

class Recommendation(models.Model):
    location_name = models.CharField(max_length=100, default='', blank=False)
    address = models.CharField(max_length=250, default='', blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)

    details = models.TextField(default="No details provided", blank=True, null=True)
    likes = models.JSONField(default=dict) #needs to store associated user
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location_name

    def get_absolute_url(self):
        return reverse("maps:list")

class Comment(models.Model):
    text = models.TextField()

    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recommendation = models.ForeignKey(Recommendation, on_delete=models.CASCADE)
    likes = models.JSONField(default=dict) #may or may not use

    def __str__(self):
        return self.text