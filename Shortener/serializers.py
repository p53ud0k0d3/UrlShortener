from django.contrib.auth.models import User

from rest_framework import serializers

class UrlAPI(object):
    def __init__(self, **kwargs):
        for field in ('long_url', 'host', 'short_url'):
            setattr(self, field, kwargs.get(field, None))

class UrlAPISerializer(serializers.Serializer):
    long_url = serializers.CharField()
    host = serializers.CharField()
    
    def create(self, validated_data):
        return UrlAPI(id=None, **validated_data)


class Url_adjuster():

    def adjust(self, url):
        if str(url[7:]).startswith('http'):
            url = url[7:]
        return url