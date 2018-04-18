#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2018-04-18 17:12:44
# @Author  : caryangBingo
# @Link    : http://example.org
# @Version : $Id$

import markdown

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def custom_markdown(values):
    return mark_safe(markdown.markdown(values, extensions=['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'], safe_mode=True, enable_attributes=False))
