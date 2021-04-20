from django.shortcuts import render
from .models import SavedRoute
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

import json

# def index_view(request):
#     return render(request, 'maps/index.html')

def default_map(request):
    mapbox_access_token = 'pk.eyJ1IjoiYm1ib2dvIiwiYSI6ImNrbWUzaG9qNjJyazMyd29qMGxrbHZvd2sifQ.oG0-1XdG-OAeNRxL0Vwz6g'
    geocodio_api_key = 'c67160ed105dde990709bc077e16a76506c7956'
    return render(request, 'maps/default.html',
                  { 'mapbox_access_token': mapbox_access_token,
                  'geocodio_api_key': geocodio_api_key })

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
            elif req_type == 'Delete route':
                return delete_route(request)
            else:
                return load_route(request)
    else:
        return HttpResponse(JsonResponse({'route_status': 'failure', 'message': 'not authenticated'}))

def save_route(request):
    try:
        map_user = request.user
        rname = request.POST['route_id']
        save_coords = request.POST['coords']
        if save_coords != '':
            new_route = SavedRoute(owner=map_user, coordinates=json.loads(request.POST['coords']), name=rname)
            new_route.save()
        else:
            return HttpResponse(JsonResponse({'route_status':'failure', 'message': 'no coordinates'}))
    except(KeyError):
        return HttpResponse(JsonResponse({'route_status':'failure', 'message': 'model error'}))
    except(IntegrityError):
        return HttpResponse(JsonResponse({'route_status':'failure', 'message': 'already exists'}))
    return HttpResponse(JsonResponse({'route_status': 'saved', 'message': f'saved {rname}'}))

def load_route(request):
    route = None
    try:
        map_user = request.user
        route = SavedRoute.objects.filter(owner=map_user, name=request.POST['route_id']).get().coordinates
    except(KeyError, SavedRoute.MultipleObjectsReturned, SavedRoute.DoesNotExist):
        return HttpResponse(JsonResponse({'route_status': 'failure'}))
    else:
        return HttpResponse(JsonResponse({'route_status': 'loaded', 'route':route}))
    
def delete_route(request):
    try:
        map_user = request.user
        num = SavedRoute.objects.filter(owner=map_user, name=request.POST['route_id']).delete()[0]
    except(KeyError, SavedRoute.DoesNotExist):
        return HttpResponse(JsonResponse({'route_status': 'failure'}))
    else:
        return HttpResponse(JsonResponse({'route_status': 'deleted', 'message': f'deleted {num} objects'}))

def get_routes(request):
    pass

def display_routes(request):
    pass
    
