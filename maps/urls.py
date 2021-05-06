from django.urls import path
from . import views
from django.views.generic import TemplateView # <--

app_name = 'maps'
urlpatterns = [
    path('', views.default_map, name='default'),
    path('persist', views.persist_route, name='persist'),
    path('get_routes', views.get_routes, name='get_routes'),
    path('uva-locations', views.uva_locations, name='uva_locations'),
    path('uva-locations-save', views.store_uva_location, name='store_uva'),
    path('uva-locations-find', views.find_uva_location, name='find_uva'),
    path('locations-geojson', views.uva_location_collection, name='geo.json'),
    path('recommendations', views.RecommendationView.as_view(), name='recommendations'),
    path('recommendations/list', views.RecommendationListView.as_view(), name='list'),
    path('recommendations/comment-or-like', views.update_rec, name='update_recommendation')
]
