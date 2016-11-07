# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list , list_delete, view_image, feed

urlpatterns = [
    url(r'^list/(?P<username>[-\w]+)$', list, name='list'),
    url(r'^feed/$', feed, name='feed'),
    url(r'^list/delete/(?P<question_id>[0-9]+)', list_delete , name='list_delete'),
    url(r'^(?P<mode>[-\w]+)/view/(?P<username>[-\w]+)/(?P<question_id>[0-9]+)', view_image , name='view_image')

]
