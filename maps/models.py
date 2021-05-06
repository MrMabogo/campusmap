# /***************************************************************************************
# *  REFERENCES
# *  URL: https://stackoverflow.com/questions/6540032/sorting-related-items-in-a-django-template
# *  Usage: Setting up functions in Recommendation model
# *
# *  URL: https://docs.djangoproject.com/en/3.2/topics/db/models/
# *  Usage: Creating the appropriate fields for models
# *
# ***************************************************************************************/
 

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
    start = models.JSONField(default=dict)
    end = models.JSONField(default=dict)

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
    CATEGORY_CHOICES = [
        ('College of Arts and Sciences', 'College of Arts and Sciences'),
        ('Dining', 'Dining'),
        ('Engineering School', 'Engineering School'),
        ('Library', 'Libraries'),
        ('Parking Garage', 'Parking'),
        ('Athletic', 'Athletic'),
        ('Housing', 'Housing'),
        ('Historical', 'Historical'),
        ('Batten School', 'Batten School'),
        ('McIntire School of Commerce', 'McIntire School of Commerce'),
        ('Music', 'Music'),
        ('Office', 'Office'),
        ('Research', 'Research'),
        ('School of Education', 'School of Education'),
        ('Architecture', 'Architecture'),
        ('Arts', 'Arts'),
        ('Law', 'Law'),
        ('Darden School of Business', 'Darden School of Business')
    ]

    location_name = models.CharField(max_length=100, default='', blank=False)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='College of Arts and Sciences', blank=False)
    address = models.CharField(max_length=250, default='', blank=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)

    details = models.TextField(default="No details provided", blank=True, null=True)
    likes = models.JSONField(default=dict) #needs to store associated user
    post_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    #tawmas https://stackoverflow.com/questions/6540032/sorting-related-items-in-a-django-template
    @property
    def sorted_comment_set(self):
        return self.comment_set.order_by('-post_date')

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
