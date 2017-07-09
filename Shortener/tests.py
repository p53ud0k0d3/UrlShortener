# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from Shortener.views import worker

# Model tests
# Form tests
# View tests

def test_worker_shortens_url_with_google():
    url = "http://7bna.net/wallpapers/cat-pictures.html"
    host = "Google"

    assert len(worker(url, host)) < len(url)
