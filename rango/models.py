from django.db import models
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.title
