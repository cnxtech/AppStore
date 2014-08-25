from django.conf.urls import patterns, include, url

from rest_framework import routers

from views import (
    GroupViewSet,
    UserViewSet,
    PermissionViewSet,
    ContentTypeViewSet
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'contenttypes', ContentTypeViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
