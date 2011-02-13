"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

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
        self.user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        
    def test_GET_blog_index(self):
        # Issue a GET request
        response = self.client.get('/blog/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)        

    def test_GET_blog_add(self):
        # Login
        self.client.login(username='john', password='johnpassword')

        # Issue a GET request
        response = self.client.get('/blog/add/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_POST_blog_add(self):
        # Login
        self.client.login(username='john', password='johnpassword')

        # Issue a POST request
        response = self.client.post('/blog/add/',{
                                                  'name': 'EntryName',
                                                  'slug': 'entry_slug',
                                                  'data': 'EntryData',
                                                  'published': True,
                                                 })

    def test_POST_blog_edit(self):
        # Issue a POST request
        response = self.client.post('/blog/edit/%d' %(self.e.id),
                                    {
                                        'name':'EntryRename',
                                        'slug':'entry_slug',
                                        'data':'EntryData',
                                        'published': True,
                                    })

    def test_POST_blog_delete(self):
        # Issue a POST request
        response = self.client.post('/blog/delete/%d' %(self.e.id))

        # Check that the response is 301 Redirect to blog_index.
        self.assertEqual(response.status_code, 301)
