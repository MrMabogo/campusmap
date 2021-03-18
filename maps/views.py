from django.shortcuts import render

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps/default.html',
                  { 'mapbox_access_token': mapbox_access_token })
