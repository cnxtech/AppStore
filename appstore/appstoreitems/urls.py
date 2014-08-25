from django.conf.urls import patterns, include, url

from rest_framework import routers

from views import (
    GroupViewSet,
    UserViewSet,
    PermissionViewSet,
    ContentTypeViewSet,
    AppStoreItemViewSet,
    VendorViewSet,
    AppImageViewSet,
    PlattformViewSet,
    VersionViewSet,
    ApiVersionViewSet
)

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'contenttypes', ContentTypeViewSet)

router.register(r'appstoreitems', AppStoreItemViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'appimages', AppImageViewSet)
router.register(r'platforms', PlattformViewSet)
router.register(r'versions', VersionViewSet)
router.register(r'apiversions', ApiVersionViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
