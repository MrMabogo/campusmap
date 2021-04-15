from django.shortcuts import render
from .models import SavedRoute
from django.contrib.auth.models import User
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
            else:
                return load_route(request)
    else:
        return HttpResponse(JsonResponse({'route_status': 'failure'}))

def save_route(request):
    try:
        map_user = User.objects.get(is_active=True, password=request.user.password)
        routeNum = 1
        last_rt = SavedRoute.objects.filter(owner=map_user).last()
        if last_rt != None:
            routeNum = last_rt.routeNumber+1
        save_coords = request.POST['coords']
        if save_coord != '':
            new_route = SavedRoute(owner=map_user, coordinates=json.loads(request.POST['coords']), routeNumber=routeNum)
            print(routeNum)
            new_route.save()
        else:
            return HttpResponse(JsonResponse({'route_status':'failure'}))
    except(KeyError, SavedRoute.DoesNotExist):
        return HttpResponse(JsonResponse({'route_status':'failure'}))
    return HttpResponse(JsonResponse({'route_status': 'saved'}))

def load_route(request):
    route = None
    try:
        map_user = None
        if request.user.is_authenticated:
            map_user = request.user
        route = SavedRoute.objects.filter(owner=map_user, routeNumber=request.POST['route_id']).get().coordinates
    except(KeyError, SavedRoute.MultipleObjectsReturned, SavedRoute.DoesNotExist):
        return HttpResponse(JsonResponse({'route_status': 'failure', 'route':[]}))
    else:
        return HttpResponse(JsonResponse({'route_status': 'loaded', 'route':route}))
    

def get_routes(request):
    pass

def display_routes(request):
    pass
    
