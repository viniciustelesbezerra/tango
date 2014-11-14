from django.test import TestCase, Client, SimpleTestCase
from rango.models import Category, Page
from django.core.urlresolvers import reverse
from django.db import models


class ModelCategoryTest(TestCase):

    def setUp(self):
        self.category = Category(name='cat name')

    def test_db_table_name(self):
        self.assertEqual(Page._meta.db_table, u'rango_page')

    def test_attrs_values(self):
        self.assertEqual(self.category.name, 'cat name')

    def test_unicode(self):
        self.assertEqual(self.category.__unicode__(), 'cat name')


class ModelPageTest(TestCase):

    def setUp(self):
        self.page = Page(title='title name')

    def test_model(self):
        self.assertEqual(self.page._meta.db_table, u'rango_page')
        self.assertEqual(self.page._meta.verbose_name, u'page')
        self.assertEqual(self.page._meta.model_name, 'page')
        self.assertEqual(self.page._meta.has_auto_field, True)

    def test_id_field(self):
        self.__field_test(self.page._meta.get_field('id'),
                          blank=True,
                          verbose_name=u'ID',
                          max_length=None,
                          type=models.fields.AutoField)

    def test_title_field(self):
        self.__field_test(self.page._meta.get_field('title'),
                          max_length=128,
                          type=models.fields.CharField)

    def test_url_field(self):
        self.__field_test(self.page._meta.get_field('url'),
                          max_length=200,
                          type=models.fields.URLField)

    def test_views_field(self):
        self.__field_test(self.page._meta.get_field('views'),
                          max_length=None,
                          type=models.fields.IntegerField)

    def test_category_field(self):
        self.__field_test(self.page._meta.get_field('category'),
                          max_length=None,
                          type=models.fields.related.ForeignKey,
                          rel_type=models.fields.related.ManyToOneRel)

    def test_attrs_values(self):
        self.assertEqual(self.page.title, 'title name')

    def test_unicode(self):
        self.assertEqual(self.page.__unicode__(), 'title name')

    def __field_test(self, field, **validators):
        self.assertEqual(field.null, False)
        self.assertEqual(field._error_messages, None)

        self.assertEqual(field.max_length, validators['max_length'])
        self.assertEqual(field.__class__, validators['type'])

        self.assertEqual(field.blank, validators.get('blank', False))
        self.assertEqual(field.rel.__class__,
                         validators.get('rel_type', type(None)))
        self.assertEqual(field._verbose_name,
                         validators.get('verbose_name', None))


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
        self.assertEqual(response.content,
                         '<b>show template for rango app</b>')
        self.assertEqual(response.context['x'], 'i am x')
        self.assertTemplateUsed(response, 'rango/show.html')
