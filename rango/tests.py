from django.test import TestCase, Client, SimpleTestCase
from rango.models import Category, Page
from django.core.urlresolvers import reverse


class ModelCategoryTest(TestCase):

    def setUp(self):
        self.category = Category(name='cat name')

    def test_attrs_values(self):
        self.assertEqual(self.category.name, 'cat name')

    def test_unicode(self):
        self.assertEqual(self.category.__unicode__(), 'cat name')


class ModelPageTest(TestCase):

    def setUp(self):
        self.page = Page(title='title name')

    def test_attrs_values(self):
        self.assertEqual(self.page.title, 'title name')

    def test_unicode(self):
        self.assertEqual(self.page.__unicode__(), 'title name')


class ViewsTestSimple(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'rango app')
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_show(self):
        response = self.client.get(reverse('show'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '<b>show template for rango app</b>')
        self.assertEqual(response.context['x'], 'i am x')
        self.assertTemplateUsed(response, 'rango/show.html')
