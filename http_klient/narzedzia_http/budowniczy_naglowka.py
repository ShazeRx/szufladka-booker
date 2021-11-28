class BudowniczyNaglowka:

    @staticmethod
    def wez_naglowek_bez_jwt(content_type: str):
        return {"Content-Type": content_type}

    @staticmethod
    def wez_naglowek_jwt(jwt: str, content_type) -> dict[str, str]:
        return {"Authorization": "Bearer {}".format(jwt)} | BudowniczyNaglowka.wez_naglowek_bez_jwt(
            content_type=content_type)
