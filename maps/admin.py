from django.contrib import admin
from .models import SavedRoute
from .models import UVALocation

# Register your models here.
admin.site.register(SavedRoute)
admin.site.register(UVALocation)