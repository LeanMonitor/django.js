# -*- coding: utf-8 -*-
import sys

from os.path import join, isdir

from django.conf.urls import url

from djangojs.conf import settings
from djangojs.views import UrlsJsonView, ContextJsonView, JsInitView

# DJANGO 1.10

from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    url(r'^init\.js$', JsInitView.as_view(), name='django_js_init'),
    url(r'^urls$', UrlsJsonView.as_view(), name='django_js_urls'),
    url(r'^context$', ContextJsonView.as_view(), name='django_js_context'),
    url(r'^translation$', JavaScriptCatalog.as_view(), name='js_catalog'),
    # url(r'^translation$', 'django.views.i18n.javascript_catalog',
    #    js_info_dict(), name='js_catalog')
]
