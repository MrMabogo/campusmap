from django.urls import path
from . import views

app_name = 'maps'
urlpatterns = [
    # path('', views.index_view, name='index'),
    path('', views.default_map, name='default'),
    path('persist', views.persist_route, name='persist'),
    path('get_routes', views.get_routes, name='get_routes'),
    path('uva-locations', views.uva_locations, name='uva_locations'),
    path('uva-locations-save', views.store_uva_location, name='store_uva'),
    path('uva-locations-find', views.find_uva_location, name='find_uva')
]
