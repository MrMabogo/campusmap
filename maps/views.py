from django.shortcuts import render

# def index_view(request):
#     return render(request, 'maps/index.html')

def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'maps/default.html',
                  { 'mapbox_access_token': mapbox_access_token })

def map_search(request):
    pass

def get_eta(request):
    pass

def save_route(request):
    pass

def get_routes(request):
    pass

def display_routes(request):
    pass
    
