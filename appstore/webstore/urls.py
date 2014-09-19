from django.conf.urls import patterns, url

from .views import (
    ListView,
    AppView
)

urlpatterns = patterns(
    '',
    url(r'^$', ListView.as_view()),
    url(r'^app/(?P<uuid>[^/]+)/$', AppView.as_view()),
)
