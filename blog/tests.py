"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
from django.test import TestCase

from Django_Blog.blog.models import Entry

class SimpleLoadURLTest(TestCase):
    def setUp(self):
        """
        Every test needs a client
        """
        self.client = Client()
        self.e = Entry.objects.create(
                                      name='EntryName',
                                      slug='entry_slug',
                                      data='EntryData',
                                      published=True
                                     )
        
    def test_GET_blog_index(self):
        # Issue a GET request
        response = self.client.get('/blog/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)        

    def test_GET_blog_add(self):
        # Issue a GET request
        response = self.client.get('/blog/add/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_POST_blog_add(self):
        # Issue a POST request
        response = self.client.post('/blog/add/',{
                                                  'name': 'EntryName',
                                                  'slug': 'entry_slug',
                                                  'data': 'EntryData',
                                                  'published': True,
                                                 })
        # Check that the response is 302 Redirect to blog_index.
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url='/blog/')

    # NOTE: IMPORTANT ---- this should be the last test (all deletes should be last)
    """
    def test_POST_blog_delete(self):
        # Issue a POST request
        response = self.client.post('/blog/delete/%d' %(self.e.id))
    """ 
        

        
