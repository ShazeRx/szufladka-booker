from http_klient.I_klient_http import IKlientHttp


class Szufladka:
    def __init__(self, i_klient_http: IKlientHttp):
        self.klient_http = i_klient_http

    def uruchom(self):
        while True:
            self._show_login_screen()

    def _show_login_screen(self):
        pass
