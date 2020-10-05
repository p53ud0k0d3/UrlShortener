# encoding: utf-8
"""
GooLNK Shortener Implementation
"""
import json

from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException


class GooLNK(BaseShortener):
    api_url = "https://goolnk.com/api/v1/shorten"

    def short(self, url):
        
        response = self._post(self.api_url, data={'url':url})

        if response.ok:
            return json.loads(response.text)['result_url']

        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))
