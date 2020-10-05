# encoding: utf-8
"""
Chogoon Shortener Implementation
"""
import json

from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException


class Chogoon(BaseShortener):
    api_url = "https://chogoon.com/srt/api/"

    def short(self, url):
        
        response = self._post(self.api_url, data={'url':url})

        if response.ok:
            return json.loads(response.text)['data']['url']

        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))
