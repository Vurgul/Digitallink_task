from rest_framework import serializers


class LinksSerializer(serializers.Serializer):
    number = serializers.CharField(max_length=15)
    found = serializers.BooleanField(default=True)
