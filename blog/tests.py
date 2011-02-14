"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test.client import Client
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site

from Django_Blog.blog.models import Entry

class SimpleLoadURLTest(TestCase):
    def setUp(self):
        """
        Every test needs a client
        """
        self.client = Client()
        self.e = Entry.objects.create(
                                      name='EntryName',
                                      slug='entry-slug',
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
                                                  'slug': 'entry-slug',
                                                  'data': 'EntryData',
                                                  'published': True,
                                                 })

    def test_POST_blog_edit(self):
        # Issue a POST request
        response = self.client.post('/blog/edit/%s' %(self.e.slug),
                                    {
                                        'name':'EntryRename',
                                        'slug':'entry-slug',
                                        'data':'EntryData',
                                        'published': True,
                                    })

    def test_POST_blog_delete(self):
        # Issue a POST request
        response = self.client.post('/blog/delete/%s' %(self.e.slug))

        # Check that the response is 301 Redirect to blog_index.
        self.assertEqual(response.status_code, 301)

    def test_GET_logout(self):
        # Issue a GET request
        response = self.client.get('/accounts/logout/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

    def test_create_comment(self):
        CT = ContentType.objects.get_for_model
        
        # Issue a POST request
        c1 = Comment.objects.create(
            content_type = CT(self.e),
            object_pk = "1",
            user_name = "Lasko",
            user_email = "bmheight@gmail.com",
            user_url = "http://example.com/~joe",
            comment = "First!",
            site = Site.objects.get_current(),
        )
        self.assertEqual(str(c1), "Lasko: First!...")
