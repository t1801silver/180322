from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from team.fields import ThumbnailImageField

# @python_2_unicode_compatible
# class PlanPost(models.Model):
#     title = models.CharField('TITLE', max_length=50)
#     slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
#     description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text.')
#     content = models.TextField('CONTENT')
#     create_date = models.DateTimeField('Create Date', auto_now_add=True)
#     modify_date = models.DateTimeField('Modify Date', auto_now=True)
#     owner = models.ForeignKey(User, null=True)
#
#     class Meta:
#         verbose_name = 'planpost'
#         verbose_name_plural = 'planposts'
#         db_table  = 'plan_posts'
#         ordering  = ['modify_date',]
#
#     def __str__(self):
#         return self.title
#
#     # def get_absolute_url(self):
#     #     return reverse('team:plan_detail', args=(self.id,))
#
#     def get_previous_post(self):
#         return self.get_previous_by_modify_date()
#
#     def get_next_post(self):
#         return self.get_next_by_modify_date()
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.slug = slugify(self.title, allow_unicode=True)
#         super(PlanPost, self).save(*args, **kwargs)
#
#     def get_absolute_url(self):
#         return reverse('team:PlanPhoto_detail', args=(self.id,))
#
#
# @python_2_unicode_compatible
# class PlanPhoto(models.Model):
#     planpost = models.ForeignKey(PlanPost)
#     title = models.CharField(max_length=50)
#     image = ThumbnailImageField(upload_to='team/%Y/%m')
#     description = models.TextField('Photo Description', blank=True)
#     upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
#     owner = models.ForeignKey(User, null=True)
#
#     class Meta:
#         ordering = ['title']
#
#     def __str__(self):
#         return self.title
#
#     def get_absolute_url(self):
#         return reverse('team:plan_detail', args=(self.id,))
