# /***************************************************************************************
# *  REFERENCES
# *  URL: https://docs.djangoproject.com/en/3.2/topics/testing/tools/
# *  Usage: Setting up tests with Django
# *
# ***************************************************************************************/

from django.test import TransactionTestCase
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from .models import SavedRoute
from django.contrib.auth.models import User

import json

def create_test_route(time, dist):
    troute = {
        'distance': dist,
        'duration': time,
        'legs': dict(),
        'geometry': dict()}
    return troute
def create_test_location(lat, lng, end): # end is either 'A' or 'B'
    location = {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [lat, lng]
        },
        "properties": {
            "id": "origin",
            "marker-symbol": end
        }
    }
    return location


class PersistenceTests(TransactionTestCase):
    def test_save_empty_route(self):
        '''
        Save route without specifying a route
        '''
        data = {
            'persist_type': 'Save route',
            'route_id': 'test',
            'coords': ''
        }
        tUser = User.objects.get_or_create(username='test', password='secret')[0]
        self.client.force_login(tUser)
        response = self.client.post(reverse('maps:persist'), data, secure=True)
        response = json.loads(response.content)
        self.assertEqual(response['route_status'], 'failure')

    def test_save_multiple_routes(self):
        '''
        Save multiple valid routes
        '''
        data = {
            'persist_type': 'Save route',
            'route_id': 'test',
            'start': json.dumps(create_test_location(-78.508696, 38.035841, 'A')),
            'end': json.dumps(create_test_location(-78.51911, 38.028773, 'B'))
            # 'coords': json.dumps(create_test_route('10', '5'))
        }
        data2 = {
            'persist_type': 'Save route',
            'route_id': 'test2',
            'start': json.dumps(create_test_location(-78.51911, 38.028773, 'A')),
            'end': json.dumps(create_test_location(-78.508696, 38.035841, 'B'))
            #'coords': json.dumps(create_test_route('10', '30'))
        }

        tUser = User.objects.get_or_create(username='test', password='secret')[0]
        self.client.force_login(tUser)

        response = self.client.post(reverse('maps:persist'), data, secure=True)
        response = json.loads(response.content)
        self.assertEqual(response['route_status'], 'saved')

        response = self.client.post(reverse('maps:persist'), data2, secure=True)
        response = json.loads(response.content)
        self.assertEqual(response['route_status'], 'saved')
