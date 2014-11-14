from django.test import Client, SimpleTestCase
from django.core.urlresolvers import reverse
from rango.models import Category


class ViewsTestSimple(SimpleTestCase):

    def setUp(self):
        self.client = Client()

    def test_index(self):
        category = self.__create_category()

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'rango app')
        self.assertContains(response, 'cn1')
        self.assertTrue(category in response.context['categories'])
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_show(self):
        response = self.client.get(reverse('show'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content,
                         '<b>show template for rango app</b>')
        self.assertEqual(response.context['x'], 'i am x')
        self.assertTemplateUsed(response, 'rango/show.html')

    def __create_category(self):
        return Category.objects.create(name='cn1')
