import json
from typing import Tuple, Any

import requests
from requests import Response

from http_klient.I_klient_http import IKlientHttp
from http_klient.api.api_stale import API_URL
from http_klient.narzedzia_http.budowniczy_naglowka import BudowniczyNaglowka
from http_klient.narzedzia_http.jwt_opiekun import JwtOpiekun


class KlientHttp(IKlientHttp):
    def __init__(self, jwt_opiekun: JwtOpiekun):
        self._api_url = API_URL
        self._jwt_opiekun = jwt_opiekun

    def post(self, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        header = BudowniczyNaglowka.wez_naglowek_bez_jwt(content_type='application/json')
        response = requests.post(url=self._build_url(url), data=body, params=params,
                                 headers=header)
        return self._handle_response(response)

    def get(self, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        response = requests.get(url=self._build_url(url), data=body, params=params,
                                headers=self._build_header_with_jwt(content_type='application/json'))
        return self._handle_response(response)

    def patch(self, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        response = requests.patch(url=self._build_url(url), data=body, params=params,
                                  headers=self._build_header_with_jwt(content_type='application/json'))
        return self._handle_response(response)

    def _build_url(self, url: str):
        return self._api_url + url

    def _handle_response(self, response: Response) -> Tuple[dict[str:Any], int]:
        status_code = response.status_code
        try:
            response_json = response.json()
        except json.decoder.JSONDecodeError:
            response_json = ""
        return response_json, status_code

    def _build_header_with_jwt(self, content_type: str) -> dict[str, str]:
        jwt = self._jwt_opiekun.pobierz_jwt()
        return BudowniczyNaglowka.wez_naglowek_jwt(jwt, content_type=content_type)
