from abc import ABC, abstractmethod


class IPrzypadekUzycia(ABC):

    @abstractmethod
    def wykonaj(self, *args, **kwargs):
        pass
