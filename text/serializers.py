from rest_framework import serializers
from .models import Text


class TextSerializer(serializers.HyperlinkedModelSerializer):

    created_at = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M", read_only=True)
    updated_at = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M", read_only=True)

    class Meta:
        model = Text
        fields = ['id', 'text', 'created_at', 'updated_at']
