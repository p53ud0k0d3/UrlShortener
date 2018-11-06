# encoding: utf-8
"""
Rebrandly Shortener Implementation
Needs a API_KEY
"""
import json

from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException


class CustomShortener(BaseShortener):
    api_url = "https://api.rebrandly.com/v1/links"


    def short(self, url):
        params = json.dumps({
            'destination': url,
            'domain': {'fullname': 'rebrand.ly'}
        })
        headers = {
            'content-type': 'application/json',
            'apikey': self.api_key
        }
        response = self._post(self.api_url, data=params, headers=headers)
        if response.ok:
            try:
                
                data = response.json()
            except ValueError as e:
                raise ShorteningErrorException('There was an error shortening'
                                               ' this url - {0}'.format(e))
            if 'shortUrl' in data:
                return data['shortUrl']
        raise ShorteningErrorException('There was an error shortening this '
                                       'url - {0}'.format(response.content))

    def expand(self, url):
        pass

    def total_clicks(self, url):
        pass
