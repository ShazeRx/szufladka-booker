class JwtOpiekun:
    def __init__(self):
        self.jwt = ""

    def zapisz_jwt(self, jwt: str):
        self.jwt = jwt

    def pobierz_jwt(self) -> str:
        return self.jwt
