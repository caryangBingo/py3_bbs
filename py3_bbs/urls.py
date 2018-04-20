# -*- coding: utf-8 -*-
# @Author: crazyBingo
# @Date:   2018-04-16 17:18:52
# @Last Modified by:   crazyBingo
# @Last Modified time: 2018-04-20 14:36:28
"""dj_web_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ablog import views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.blog_home, name='blog_home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    #url(r'^(?P<my_args>\d+)/$', views.detail, name='detail'),
    url(r'^ablog/$', views.ablog, name='ablog'),
    url(r'^aboutMe/$', views.aboutMe, name='aboutMe'),
    url(r'^tag/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^feed/$', views.rssfeed(), name="RSS"),
]
