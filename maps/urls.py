from django.conf.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('maps/', views.default_map, name="default"),
]
