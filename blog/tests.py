"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.utils import unittest
from django.test.client import Client

class SimpleLoadURLTest(unittest.TestCase):
    def setUp(self):
        """
        Every test needs a client
        """
        self.client = Client()

    def test_blog_index(self):
        # Issue a GET request
        response = self.client.get('/blog/')

        # Check that the response id 200 OK.
        self.assertEqual(response.status_code, 200)        

        
