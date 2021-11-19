from abc import abstractmethod, ABC
from typing import Any, Tuple


class IKlientHttp(ABC):
    @abstractmethod
    def post(self, jwt: str, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        pass

    def get(self, jwt: str, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        pass

    def patch(self, jwt: str, url: str, body: str = None, params=None) -> Tuple[dict[str:Any], int]:
        pass
