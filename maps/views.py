from django.shortcuts import render
from .models import SavedRoute
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

import json

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
    pass

def save_route(request):
    pass

def load_route(request):
    pass

def get_routes(request):
    pass

def display_routes(request):
    pass
    
