# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import list , list_delete, view_image, feed , save_comment , follow , unfollow
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^list/(?P<username>[-\w]+)$', list, name='list'),
    url(r'^feed$', feed, name='feed'),
    url(r'^list/delete/(?P<question_id>[0-9]+)', list_delete , name='list_delete'),
    url(r'^(?P<mode>[-\w]+)/view/(?P<username>[-\w]+)/(?P<question_id>[0-9]+)', view_image , name='view_image'),
    url(r'^savecomment/(?P<question_id>[0-9]+)/(?P<mode>[-\w]+)$', save_comment, name='save_comment'),
    url(r'^list/follow/(?P<username>[-\w]+)$', follow, name='follow'),
    url(r'^list/unfollow/(?P<username>[-\w]+)$', unfollow, name='unfollow'),


]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
