from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

from design.fields import ThumbnailImageField

from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class DesignAlbum(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('design:album_detail', args=(self.id,))

@python_2_unicode_compatible
class DesignPhoto(models.Model):
    album = models.ForeignKey(DesignAlbum)
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('design:photo_detail', args=(self.id,))
