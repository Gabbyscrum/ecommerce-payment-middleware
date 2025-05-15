from abc import ABC, abstractmethod

class Repository(ABC):

    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(self, key: str, value: dict):
        pass
