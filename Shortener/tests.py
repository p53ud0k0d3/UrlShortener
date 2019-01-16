# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from urllib.parse import urlparse

from django.core.validators import URLValidator

import pytest
from Shortener.views import worker

URL = 'http://7bna.net/wallpapers/cat-pictures.htm'


@pytest.mark.parametrize('host,url', [
    ('Google', URL),
    ('Bitly', URL),
    ('Madwire', URL),
    ('Rebrandly', URL),
    ('isgd', URL),
])
def test_worker_shortens_url_with_(host, url):
    shortened_url = worker(url, host)
    assert url_validator(shortened_url)
    assert len(shortened_url) < len(url)


def url_validator(url):
    try:
        result = urlparse(url)
        return True if [result.scheme, result.netloc, result.path] else False
    except:
        return False
