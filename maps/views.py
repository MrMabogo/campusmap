from django.shortcuts import render
from .models import MapUser, SavedRoute
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

import json
import logging

logger = logging.getLogger(__name__)

# def index_view(request):
#     return render(request, 'maps/index.html')

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoiYm1ib2dvIiwiYSI6ImNrbWUzaG9qNjJyazMyd29qMGxrbHZvd2sifQ.oG0-1XdG-OAeNRxL0Vwz6g'
    return render(request, 'maps/default.html',
                  { 'mapbox_access_token': mapbox_access_token })

def map_search(request):
    pass

def get_eta(request):
    pass

def persist_route(request):
    if request.user.is_authenticated:
        try:
            req_type = request.POST['persist_type']
        except(KeyError):
            return render(request, 'maps/index.html')
        else:
            if req_type == 'Save route':
                return save_route(request)
            else:
                return load_route(request)
    else:
        return HttpResponseRedirect(reverse('maps:default'))

def save_route(request):
    try:
        map_user = MapUser.objects.get(is_active=True, password=request.user.password)
        new_route = SavedRoute(owner=map_user)
        new_route.coordinates = json.loads(request.POST['coords'])
    except(KeyError, SavedRoute.DoesNotExist):
        pass
    return HttpResponse("saved")

def load_route(request):
    route = None
    try:
        map_user = MapUser.objects.get(is_active=True, password=request.user.password)
    except(KeyError):
        pass
    else:
        route = json.load(list(SavedRoute.objects.get(owner=map_user))[0])

    return HttpResponse(route)
    

def get_routes(request):
    pass

def display_routes(request):
    pass
    
