# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from pyshorteners import Shortener
from .forms import Urlform

BITLY_TOKEN = "19c73c3f96d4b2a64d0337ef7380cf0de313e8f7"

def worker(url, host):
    if host == "Bitly":
        shortener = Shortener("Bitly", timeout=10, bitly_token=BITLY_TOKEN)
    else:
        shortener = Shortener(host, timeout=10)
    short_url = shortener.short(url)
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


