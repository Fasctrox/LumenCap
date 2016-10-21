from comments.views import save
from comments.views import comments

from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^comments/$', 'comments.views.comments'),
    url(r'^save/$', 'comments.views.save'),
)