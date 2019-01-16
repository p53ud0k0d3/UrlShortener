# encoding: utf-8
"""
Google Shortener Implementation
Needs a API_KEY
"""
import json
from requests.exceptions import RequestException
from pyshorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException


class Google(BaseShortener):
    api_url = "https://www.googleapis.com/urlshortener/v1/url"

    def __init__(self, **kwargs):
        if not kwargs.get('api_key', False):
            raise TypeError('api_key missing from kwargs')
        self.api_key = kwargs.get('api_key')
        super(Google, self).__init__(**kwargs)

    def short(self, url):
        params = '{}={}'.format('key', self.api_key) # to not encode
        data = json.dumps({'longUrl': url})
        headers = {'content-type': 'application/json'}
        try:
            response = self._post(
                self.api_url,
                params=params,
                data=data,
                headers=headers
            )
            response.raise_for_status()
        except (ValueError,KeyError,RequestException) as e:
            raise ShorteningErrorException('There was an error shortening'
                                           ' this url - {0}'.format(e))
        else:
            return response.json()['id']

    def expand(self, url):
        pass

    def total_clicks(self, url):
        pass
