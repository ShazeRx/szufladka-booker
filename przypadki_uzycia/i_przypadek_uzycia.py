from abc import ABC, abstractmethod


class IUseCase(ABC):

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass