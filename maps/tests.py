from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import SavedRoute
from django.contrib.auth.models import User

import json

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
        Save route without specifying
        '''
        request = HttpRequest()
        request.POST['persist_type'] = 'Save route'
        request.POST['coords'] = ''
        response = json.loads(self.client.get(reverse('maps:persist')).content)

        self.assertEqual(response, {'route_status': 'failure'})
    def test_save_multiple_routes(self):
        '''
        Save multiple valid routes
        '''
        self.assertIs(True, True) #placeholder
