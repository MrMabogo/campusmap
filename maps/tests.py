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
        response = self.client.post(reverse('maps:persist'), secure=True, data)
        response = json.loads(response.content)
        self.assertEqual(response['route_status'], 'failure')

    def test_save_multiple_routes(self):
        '''
        Save multiple valid routes
        '''
        data = {
            'persist_type': 'Save route',
            'route_id': 'test',
            'coords': json.dumps(create_test_route('10', '5'))
        }
        data2 = {
            'persist_type': 'Save route',
            'route_id': 'test2',
            'coords': json.dumps(create_test_route('10', '30'))
        }

        tUser = User.objects.get_or_create(username='test', password='secret')[0]
        self.client.force_login(tUser)

        response = self.client.post(reverse('maps:persist'), secure=True, data)
        response = json.loads(response.content)
        self.assertEqual(response['route_status'], 'saved')

        response = self.client.post(reverse('maps:persist'), secure=True, data2)
        response = json.loads(response.content)
        self.assertEqual(response['route_status'], 'saved')
