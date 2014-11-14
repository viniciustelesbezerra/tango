from django.contrib import admin
from django.test import TestCase
from rango.admin import CategoryAdmin


class CategoryAdminTest(TestCase):

    def setUp(self):
        self.category_admin = CategoryAdmin

    def test_prepopulated_fields(self):
        self.assertEquals(self.category_admin.prepopulated_fields,
                          {'slug': ('name',)})

    def test_registered_on_site(self):
        self.assertEquals(admin.site._registry, {})
