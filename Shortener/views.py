# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from pyshorteners import Shortener
from .forms import Urlform, HOSTS

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UrlAPISerializer
from .services.rebrandly import Rebrandly
from .services.madwire import Madwire
from django.core.validators import URLValidator

validate = URLValidator()
# from pyshorteners.exceptions import UnknownShortenerException


BITLY_TOKEN = "19c73c3f96d4b2a64d0337ef7380cf0de313e8f7"
GOOGLE_TOKEN = "AIzaSyCyj45kuk95kopaSuJ4NvErGMyTVV9i3n4"
REBRANDLY_TOKEN = "b71d7dcfd2f14f0ca4f533bbd6fd226a"

def worker(url, host):          # Madwire, Google, and Rebrandly no longer supported by pyshortener
    try:                     #Check if the url is valid or not
        validate(url)
    except:
        return "Invalid URL"

    shortener = Shortener()
    if host == "Bitly":
        shortener = Shortener(api_key=BITLY_TOKEN)
        short_url = shortener.bitly.short(url)
    elif host == "Isgd":
        short_url = shortener.isgd.short(url)
    # elif host == "Madwire":
    #     shortener = Shortener(engine=Madwire, timeout=10)
    # elif host == "Rebrandly": no longer supported by pyshortener
    #     shortener = Shortener(engine=Rebrandly, timeout=10, api_key=REBRANDLY_TOKEN)
    elif host == "Tinyurl":
        short_url = shortener.tinyurl.short(url)
    else:
        short_url = "That service is no longer available via pyshortener"
    return short_url


def home(request):
    template = 'shortener/home.html'

    if request.method == 'GET':
        form_class = Urlform()
    else:
        form_class = Urlform(request.POST)

        if form_class.is_valid():
            url = form_class.cleaned_data['url']
            host = form_class.cleaned_data['host']
            short_url = worker(url, host)
            form_class = Urlform()
            return render(request, template, {'form': form_class, 'short_url': short_url,})

    return render(request, template, {'form': form_class,})


class UrlShortenerAPIViewSet(viewsets.ViewSet):
    """
    Shortens URL via a POST method.
    
    Provide the following fields in your POST request:
    "long_url": "URL to shorten, Example: https://www.youtube.com/watch?v=Y2VF8tmLFHw", 
    "host": "Shortening service to use, must be one of: [hosts]"
    
    Returns:
    "short_url": "Shortened URL"
    """
    hostsString = ""
    for host in HOSTS: hostsString += host[0] + " "
    __doc__ = __doc__.replace("[hosts]", hostsString)
    
    def create(self, request, format=None):
        serializer = UrlAPISerializer(data=request.data)
        if serializer.is_valid():
            UrlAPIObject = serializer.create(serializer.data)
            try:
                ShortURL = worker(UrlAPIObject.long_url, UrlAPIObject.host)
            except (TypeError):
                return Response({'error': u'host must be one of: ' + self.hostsString}, status=status.HTTP_400_BAD_REQUEST)
            except ValueError:
                return Response({'error': u'url invalid, please use a valid url'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'short_url': str(ShortURL)}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
