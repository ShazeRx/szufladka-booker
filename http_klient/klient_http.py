from typing import Tuple, Any
import requests
from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import API_URL


class KlientHttp(IKlientHttp):
    def __init__(self):
        self._api_url = API_URL

    def post(self, jwt: str, body: str, url: str) -> Tuple[dict[str:Any], int]:
        response = requests.post(url=self._build_url(url), data=body)
        return response.json(), response.status_code

    def get(self, jwt: str, body: str, url: str) -> Tuple[dict[str:Any], int]:
        pass

    def patch(self, jwt: str, body: str, url: str) -> Tuple[dict[str:Any], int]:
        pass

    def _build_url(self, url: str):
        return self._api_url + url
