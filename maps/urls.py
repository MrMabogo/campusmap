from django.urls import path
from . import views

app_name = 'maps'
urlpatterns = [
    # path('', views.index_view, name='index'),
    path('', views.default_map, name="default"),
    path('persist', views.persist_route, name="persist"),
    path('get_routes', views.get_routes, name='get_routes')
]
