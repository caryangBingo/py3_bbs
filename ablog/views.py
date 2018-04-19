# -*- coding: utf-8 -*-
# @Author: crazyBingo
# @Date:   2018-04-17 09:52:03
# @Last Modified by:   crazyang
# @Last Modified time: 2018-04-19 18:34:42
from django.shortcuts import render
from django.http import HttpResponse
from ablog.models import AEblog
from datetime import datetime
# Create your views here.


def blog_home(request):
    # return HttpResponse("Welcome Here!!!")
    post_list = AEblog.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = AEblog.objects.get(id=str(id))
    except AEblog.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def ablog(request):
    try:
        post_list = AEblog.objects.all()
    except AEblog.DoesNotExist:
        raise Http404
    return render(request, 'ablog.html', {'post_list': post_list, 'error': False})


def aboutMe(request):
    return render(request, 'about_me.html')


def search_tag(request, tag):
    try:
        post_list = AEblog.objects.filter(category__iexact=tag)
    except AEblog.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list': post_list})


"""
def detail(request, my_args):
    # return HttpResponse("You're looking at my_args %s." % my_args)
    post = AEblog.objects.all()[int(my_args)]
    str = ("title=%s,category=%s,date_time=%s,content=%s" %
           (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)


def test(request):
    return render(request, 'home.html', {'post_list': post_list})
"""
