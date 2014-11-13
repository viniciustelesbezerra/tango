import unittest2
from django.test import Client
from django.core.urlresolvers import reverse


class ViewsTest(unittest2.TestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'Rango says hey there world!')

    def test_show(self):
        response = self.client.get(reverse('show'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, 'show template for rango app')
        self.assertTrue(any('rango/show.html' in t.name
                            for t in response.templates))
