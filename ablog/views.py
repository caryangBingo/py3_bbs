# -*- coding: utf-8 -*-
# @Author: crazyBingo
# @Date:   2018-04-17 09:52:03
# @Last Modified by:   crazyang
# @Last Modified time: 2018-06-12 16:42:36
from django.shortcuts import render
from django.http import HttpResponse
from ablog.models import AEblog
from datetime import datetime
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def blog_home(request):
    # return HttpResponse("Welcome Here!!!")
    post_list = AEblog.objects.all()
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
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


def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = AEblog.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'ablog.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'ablog.html', {'post_list': post_list, 'error': False})
        return redirect('/')


class rssfeed(Feed):
    title = "RSS Feed-ablog"
    link = "feeds/posts/"
    description = "RSS Feed-blog posts"

    def items(self):
        return AEblog.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content


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
