from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import SavedRoute
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.backends import ModelBackend

import json

def create_test_route(time, dist):
    troute = {
        'distance': dist,
        'duration': time,
        'legs': dict(),
        'geometry': dict()}
    return json.dumps(troute)

class NavigationTests(TestCase):
    def test_search_for_fake_location(self):
        '''
        Expected arrival to location that doesn't exist
        '''
        self.assertIs(True, True) #placeholder

    def test_eta_to_here(self):
        '''
        Expected arrival to current location
        '''
        self.assertIs(True, True) #placeholder

    def test_multiple_etas(self):
        '''
        Expected arrival to multiple different locations
        '''
        self.assertIs(True, True) #placeholder

    def test_save_empty_route(self):
        '''
        Save route without specifying a route
        '''
        request = HttpRequest()
        request.POST['persist_type'] = 'Save route'
        request.POST['route_id'] = 'test'
        request.POST['coords'] = ''
        response = json.loads(self.client.get(reverse('maps:persist'), secure=True).content)

        self.assertEqual(response['route_status'], 'failure')

    def test_save_multiple_routes(self):
        '''
        Save multiple valid routes
        '''
        self.assertIs(True, True) #placeholder