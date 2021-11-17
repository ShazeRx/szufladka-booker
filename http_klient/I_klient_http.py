from abc import abstractmethod, ABC


class IKlientHttp(ABC):
    @abstractmethod
    def post(self):
        pass

    def get(self):
        pass
