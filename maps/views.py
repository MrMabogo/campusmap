from django.shortcuts import render, get_object_or_404
from .models import SavedRoute, UVALocation, UVALocationCollection, Recommendation, Comment
from django.contrib.auth.models import User
from django.contrib.postgres.search import SearchVector
from django.db.models import TextField
from django.db.models.functions import Cast
from django.db import IntegrityError
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import RecommendationPostingForm
from django.views import generic

import json

def default_map(request):
    saved = dict()
    if request.user.is_authenticated:
        saved = SavedRoute.objects.filter(owner=request.user)
    mapbox_access_token = 'pk.eyJ1IjoiYm1ib2dvIiwiYSI6ImNrbWUzaG9qNjJyazMyd29qMGxrbHZvd2sifQ.oG0-1XdG-OAeNRxL0Vwz6g'
    geocodio_api_key = 'c67160ed105dde990709bc077e16a76506c7956'
    return render(request, 'maps/default.html',
                  { 'mapbox_access_token': mapbox_access_token,
                  'geocodio_api_key': geocodio_api_key,
                  'savedroutes':  saved})

def uva_locations(request):
    if request.user.is_superuser:
        return render(request, 'maps/load-uva-locations.html')
    else:
        return Http404

def uva_location_collection(request):
    try:
        locations = UVALocationCollection.objects.first().geojson
    except:
        raise Http404
    else:
        return JsonResponse(locations)

def find_uva_location(request):
    #https://stackoverflow.com/questions/38835167/django-fulltext-search-on-json-field
    try:
        status = 'found'
        keyword = request.POST['keyword']
        last_match = UVALocation.objects.annotate(search=SearchVector(Cast('properties', TextField())))
        keywords = keyword.split(',')

        #progressively filter for each word
        for keyphrase in keywords:
            for kw in keyphrase.split(' '):
                stripped = kw.strip()
                if stripped != '':
                    cur_match = last_match.filter(search=stripped)

                    if cur_match.exists():
                        last_match = cur_match
                    else:
                        status = 'approximate'
                        break
    except(KeyError):
            return render(request, 'maps/index.html')
    else:
        result = last_match.first()
        return HttpResponse(JsonResponse({
            'location_status': status,
            'location': {'coordinates': result.coordinates, 'properties': result.properties}
        }))


def store_uva_location(request):
    try:
        if request.POST['type'] == 'single':
            jsondict = json.loads(request.POST['geojson'])
            new_location = UVALocation(
                name=jsondict['properties']['name'],
                coordinates=jsondict['geometry']['coordinates'],
                properties=jsondict['properties'])
            new_location.save()
        elif request.POST['type'] == 'full':
            jsondict = json.loads(request.POST['geojson'])
            UVALocationCollection.objects.all().delete() #there should only be one
            new_collection = UVALocationCollection(geojson=jsondict)
            new_collection.save()
        else:
            return HttpResponse(JsonResponse({'status':409, 'message': 'no type'}))
    except:
        return HttpResponse(JsonResponse({'status':409, 'message':'database exception'}))
    else:
        return HttpResponse(JsonResponse({'status':200}))


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
            new_route = SavedRoute(owner=map_user, geojson=json.loads(request.POST['coords']), name=rname)
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
        route = SavedRoute.objects.filter(owner=map_user, name=request.POST['route_id']).get().geojson
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
    #can only be called after a successful save_route
    try:
        map_user = request.user
        routes = SavedRoute.objects.filter(owner=map_user).values()
    except(KeyError, SavedRoute.DoesNotExist):
        return HttpResponse(JsonResponse({'route_status': 'failure'}))
    else:
        return HttpResponse(JsonResponse({'route_status': 'loaded', 'routes': list(routes)}))

class RecommendationView(generic.CreateView):
    model = Recommendation
    form_class = RecommendationPostingForm
    template_name = 'maps/recommendations.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        new_likes = list([self.object.author.username])
        new_likes = json.dumps(new_likes)
        self.object.likes = json.loads(new_likes)
        self.object.save()
        return super().form_valid(form)

class RecommendationListView(generic.ListView):
    model = Recommendation
    template_name = 'maps/list.html'
    context_object_name = 'latest_recommendations_list'
    queryset = Recommendation.objects.all()


# class UVALocationCollectionView(generic.CreateView):
#     model = UVALocationCollection
#     queryset = UVALocationCollection.objects.all()


def update_rec(request):
    try:
        rec = Recommendation.objects.filter(
                location_name=request.POST['name'],
                author__username=request.POST['author']
                ).get()

        if request.POST['update_type'] == 'like':    
            old_likes = rec.likes
            if request.user.username not in old_likes:
                old_likes.append(request.user.username)
                rec.likes = json.loads(json.dumps(old_likes))
                num_likes = len(old_likes)
                rec.save()
                return HttpResponse(JsonResponse({'update_status': 'liked', 'likes': num_likes}))
            else:
                return HttpResponse(JsonResponse({'update_status': 'failure', 'message': 'already liked'}))
        elif request.POST['update_type'] == 'comment':
            new_comment = Comment(author=request.user, recommendation=rec)
            new_comment.text = request.POST['comment']
            new_comment.save()
            return HttpResponseRedirect(reverse('maps:list'))
    except(KeyError, Recommendation.DoesNotExist):
        return HttpResponseRedirect(reverse('maps:list'))