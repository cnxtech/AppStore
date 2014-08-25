from rest_framework import viewsets

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType


class PermissionViewSet(viewsets.ModelViewSet):
    model = Permission


class UserViewSet(viewsets.ModelViewSet):
    model = User


class GroupViewSet(viewsets.ModelViewSet):
    model = Group


class ContentTypeViewSet(viewsets.ModelViewSet):
    model = ContentType