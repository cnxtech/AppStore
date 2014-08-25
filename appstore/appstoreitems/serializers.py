from rest_framework import serializers

from .models import AppStoreItem


class AppStoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppStoreItem
        depth = 1
