# -*- coding: utf-8 -*-
# @Author: crazyBingo
# @Date:   2018-04-17 09:52:03
# @File Name:   models.py
# @Last Modified time: 2018-04-22 23:12:12
#from mongoengine import DBNAME
from django.db import models
from django.core.urlresolvers import reverse
#from __future__ import unicode_literals
from mongoengine import Document, StringField, IntField, ListField
from mongoengine import *
from py3_bbs.settings import DBNAME


class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name

# Create your models here.


"""
class AEblog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
"""
connect(DBNAME)
#connect('mzitulg', host='mongodb://%:%')


class AEblog(Document):
    htmlTitle = StringField(max_length=50)
    startPage = StringField(max_length=50)
    imageUrls = StringField(max_length=100)
    createTime = DateTimeField(required=True)
    #content = models.TextField(blank=True, null=True)

    meta = {'collection': 'xyztulg'}

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title.encoding('utf-8')

    class Meta:
        ordering = ['-date_time']
