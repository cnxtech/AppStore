from django.db import models


class Plattform(models.Model):
    name = models.CharField(max_length=30)


class AppImage(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField()


class AppStoreItem(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    images = models.ManyToManyField(AppImage)
    platforms = models.ManyToManyField(Plattform)
