from django.contrib import admin
from .models import SavedRoute, UVALocation, UVALocationCollection

# Register your models here.
admin.site.register(SavedRoute)
admin.site.register(UVALocation)
admin.site.register(UVALocationCollection)