import json

from pyshorteners.shorteners.base import BaseShortener
from pyshorteners.exceptions import ShorteningErrorException

class bitdo(BaseShortener):
    api_url = 'https://bit.do/'

    def _init_(self, **kwargs):
        super(bitdo, self)._init_(**kwargs)

    def short(self, url):
        params =
        {
            'link': url
        }
        
        response = self._post(self.api_url, data=params)

        if response.ok:
            return 'https://' + response.text

        raise ShorteningErrorException('There was an error shortening this ''url - {0}'.format(response.content))

    def expand(self, url):
        pass

    def total_clicks(self, url):
        pass
