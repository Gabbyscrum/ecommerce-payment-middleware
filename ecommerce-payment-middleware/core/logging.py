from abc import ABC, abstractmethod

class PaymentProvider(ABC):

    @abstractmethod
    def charge(self, payload: dict) -> dict:
        pass

    @abstractmethod
    def verify_webhook(self, headers: dict, body: bytes) -> bool:
        pass
