from django.db import models

from django_extensions.db.fields import UUIDField


class Plattform(models.Model):
    name = models.CharField(max_length=30)


class AppImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()


class ApiVersion(models.Model):
    version_no = models.CharField(max_length=10)


class Version(models.Model):
    version_no = models.CharField(max_length=10)
    api_version = models.ManyToManyField(ApiVersion)
    changelog = models.TextField()


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=200, blank=True)


class AppStoreItem(models.Model):
    vendor = models.ForeignKey(Vendor)
    name = models.CharField(max_length=100)
    desc = models.TextField(verbose_name="About")
    images = models.ManyToManyField(AppImage)
    platforms = models.ManyToManyField(Plattform)
    versions = models.ManyToManyField(Version)
    uuid = UUIDField()
    url = models.URLField(max_length=200)
