# -*- coding: utf-8 -*-
# @Author: crazyBingo
# @Date:   2018-04-17 09:52:03
# @File Name:   models.py
# @Last Modified time: 2018-04-18 15:51:00
from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class AEblog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id': self.id})
        return "http://127.0.0.1:8000/%s" % path

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
