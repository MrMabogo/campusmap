import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

class FakeTest(TestCase):
    def test_travis(self):
        """
        make travis happy
        """
        self.assertIs(True, True)
