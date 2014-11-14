from django.test import TestCase
from rango.models import Category, Page
from django.db import models


class ModelTestSupport(TestCase):

    def model_default_test(self, instance):
        self.assertEqual(instance.db_table,
                         u'rango_' + instance.model_name)
        self.assertEqual(instance.verbose_name,
                         u'' + instance.model_name)
        self.assertEqual(instance.has_auto_field, True)

    def field_test(self, field, **validators):
        self.assertEqual(field.null, False)
        self.assertEqual(field._error_messages, None)

        self.assertEqual(field.max_length, validators['max_length'])
        self.assertEqual(field.__class__, validators['type'])

        self.assertEqual(field.blank, validators.get('blank', False))
        self.assertEqual(field.unique, validators.get('unique', False))

        self.assertEqual(field.rel.__class__,
                         validators.get('rel_type', type(None)))
        self.assertEqual(field._verbose_name,
                         validators.get('verbose_name', None))


class ModelCategoryTest(ModelTestSupport):

    def setUp(self):
        self.category = Category(name='cat name')

    def test_model(self):
        self.model_default_test(self.category._meta)

    def test_id_field(self):
        self.field_test(self.category._meta.get_field('id'),
                        blank=True, verbose_name=u'ID',
                        max_length=None, unique=True,
                        type=models.fields.AutoField)

    def test_name_field(self):
        self.field_test(self.category._meta.get_field('name'),
                        max_length=128,
                        unique=True,
                        type=models.fields.CharField)

    def test_views_field(self):
        self.field_test(self.category._meta.get_field('views'),
                        max_length=None,
                        type=models.fields.IntegerField)

    def test_likes_field(self):
        self.field_test(self.category._meta.get_field('likes'),
                        max_length=None,
                        type=models.fields.IntegerField)

    def test_slug_field(self):
        self.field_test(self.category._meta.get_field('slug'),
                        max_length=50, unique=True,
                        type=models.fields.SlugField)

    def test_attrs_values(self):
        self.assertEqual(self.category.name, 'cat name')

    def test_unicode(self):
        self.assertEqual(self.category.__unicode__(), 'cat name')


class ModelPageTest(ModelTestSupport):

    def setUp(self):
        self.page = Page(title='title name')

    def test_model(self):
        self.model_default_test(self.page._meta)

    def test_id_field(self):
        self.field_test(self.page._meta.get_field('id'),
                        blank=True, verbose_name=u'ID',
                        max_length=None, unique=True,
                        type=models.fields.AutoField)

    def test_title_field(self):
        self.field_test(self.page._meta.get_field('title'),
                        max_length=128,
                        type=models.fields.CharField)

    def test_url_field(self):
        self.field_test(self.page._meta.get_field('url'),
                        max_length=200,
                        type=models.fields.URLField)

    def test_views_field(self):
        self.field_test(self.page._meta.get_field('views'),
                        max_length=None,
                        type=models.fields.IntegerField)

    def test_category_field(self):
        self.field_test(self.page._meta.get_field('category'),
                        max_length=None,
                        type=models.fields.related.ForeignKey,
                        rel_type=models.fields.related.ManyToOneRel)

    def test_attrs_values(self):
        self.assertEqual(self.page.title, 'title name')

    def test_unicode(self):
        self.assertEqual(self.page.__unicode__(), 'title name')
