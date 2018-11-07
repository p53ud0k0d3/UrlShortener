# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from urllib.parse import urlparse
from django.core.validators import URLValidator
from Shortener.views import worker
from .forms import HOSTS

# Model tests
# Form tests
# View tests

def test_worker_shortens_url():
    url = "http://7bna.net/wallpapers/cat-pictures.html"

    for host, _ in HOSTS:
        shortened_url = worker(url, host)
        assert url_validator(shortened_url)
        assert len(shortened_url) < len(url)


def url_validator(url):
    try:
        result = urlparse(url)
        return True if [result.scheme, result.netloc, result.path] else False
    except:
        return False
