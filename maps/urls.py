from django.urls import path
from . import views

app_name = 'maps'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('', views.default_map, name="default"),
]
