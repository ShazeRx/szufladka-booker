import json
from typing import Tuple, Any

import requests
from requests import Response

from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import API_URL


class KlientHttp(IKlientHttp):
    def __init__(self):
        self._api_url = API_URL

    def post(self, jwt: str, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        response = requests.post(url=self._build_url(url), data=body, params=params)
        return self.handle_response(response)

    def get(self, jwt: str, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        response = requests.get(url=self._build_url(url), data=body, params=params)
        return self.handle_response(response)

    def patch(self, jwt: str, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        response = requests.patch(url=self._build_url(url), data=body, params=params)
        return self.handle_response(response)

    def _build_url(self, url: str):
        return self._api_url + url

    def handle_response(self, response: Response) -> Tuple[dict[str:Any], int]:
        status_code = response.status_code
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            response_json = ""
        return response_json, status_code
