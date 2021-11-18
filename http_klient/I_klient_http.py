from abc import abstractmethod, ABC
from typing import Any, Union, Tuple


class IKlientHttp(ABC):
    @abstractmethod
    def post(self, jwt: str, body: str,url:str) -> Tuple[dict[str:Any], int]:
        pass

    def get(self, jwt: str, body: str,url:str) -> Tuple[dict[str:Any], int]:
        pass

    def patch(self, jwt: str, body: str,url:str) -> Tuple[dict[str:Any], int]:
        pass
