from django.conf.urls import patterns, url

from .views import BaseView

urlpatterns = patterns(
    '',
    url(r'^', BaseView.as_view()),
)
