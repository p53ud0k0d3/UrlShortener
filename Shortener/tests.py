# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import itertools

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

import pytest
from pyshorteners import Shortener
from Shortener.views import worker

URL = 'http://7bna.net/wallpapers/cat-pictures.html'
# TODO get via modules
SUPPORTED_SHORTNERS = ('Google', 'Bitly', 'Madwire',)  # not including Rebandly as not idempotent
_PYSHORTNERS = set(Shortener().available_shorteners)
# TODO get via modules
_PYSHORTNERS_AUTHD = {'adfly', 'bitly', 'post', 'owly', 'tinycc', 'soogd'}
_PYSHORTNERS_UNAUTHD = _PYSHORTNERS - _PYSHORTNERS_AUTHD

TEST_PARAMS = list(zip(
    itertools.chain(SUPPORTED_SHORTNERS, _PYSHORTNERS_UNAUTHD),
    itertools.repeat(URL)
))


@pytest.mark.parametrize('host,url', TEST_PARAMS)
def test_worker_shortens_url_with_(host, url):
    shortened_url = worker(url, host)
    assert url_validator(shortened_url)
    assert len(shortened_url) < len(url)


def url_validator(url):
    try:
        URLValidator()(url)
    except ValidationError:
        return False
    else:
        return True
