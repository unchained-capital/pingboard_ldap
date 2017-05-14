from os      import environ
from os.path import join

from .log    import *
from .errors import *

try:
    import requests
except ImportError as e:
    LOG.error("{}.  Have you run 'make' yet?".format(e.mesage))
    exit(1)

# http://docs.pingboard.apiary.io/
class API(object):

    AUTH_BASE_URL   = "https://app.pingboard.com/oauth"
    APP_BASE_URL    = "https://app.pingboard.com/api/v2"
    REQUEST_HEADERS = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    def __init__(self, client_id, client_secret):
        self.client_id     = client_id
        self.client_secret = client_secret
        self._fetch_access_token()

    def request(self, method, path, params=None, data=None):
        return self._base_request(method,
                                  self.APP_BASE_URL,
                                  path,
                                  headers=dict(Authorization='Bearer {}'.format(self.access_token)),
                                  params=params,
                                  data=data)

    def _fetch_access_token(self):
        if self.client_id is None or len(self.client_id.strip()) == 0:
            raise ConfigurationError("Must provide a value for 'pingboard.id' in your configuration file.")
        if self.client_secret is None or len(self.client_secret.strip()) == 0:
            raise ConfigurationError("Must provide a value for 'pingboard.secret' in your configuration file.")
        response = self._base_request('POST',
                                      self.AUTH_BASE_URL,
                                      'token',
                                      params=dict(grant_type='client_credentials'),
                                      data=dict(client_id=self.client_id, client_secret=self.client_secret))
        self.access_token = response.get('access_token')
        
    def _base_request(self, method, base_url, path, headers=None, params=None, data=None):
        url         = join(base_url, path)
        all_headers = self.REQUEST_HEADERS.copy()
        if headers is not None:
            all_headers.update(headers)
        response =  getattr(requests, method.lower())(url, headers=all_headers, params=params, data=data)
        if response.status_code == 200:
            return response.json()
        else:
            raise APIError("Received a {} response from the Pingboard API: {}".format(response.status_code, response.text.strip()))
