from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from rest_framework import viewsets

from .models import (
    AppStoreItem,
    Vendor,
    AppImage,
    Plattform,
    Version,
    ApiVersion
)


class UserViewSet(viewsets.ModelViewSet):
    model = User


class GroupViewSet(viewsets.ModelViewSet):
    model = Group


class PermissionViewSet(viewsets.ModelViewSet):
    model = Permission


class ContentTypeViewSet(viewsets.ModelViewSet):
    model = ContentType


class AppStoreItemViewSet(viewsets.ModelViewSet):
    model = AppStoreItem


class VendorViewSet(viewsets.ModelViewSet):
    model = Vendor


class AppImageViewSet(viewsets.ModelViewSet):
    model = AppImage


class PlattformViewSet(viewsets.ModelViewSet):
    model = Plattform


class VersionViewSet(viewsets.ModelViewSet):
    model = Version


class ApiVersionViewSet(viewsets.ModelViewSet):
    model = ApiVersion
