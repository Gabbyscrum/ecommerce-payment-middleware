from abc import ABC, abstractmethod

class PaymentProvider(ABC):

    @abstractmethod
    def charge(self, payload: dict) -> dict:
        pass

    @abstractmethod
    def verify_webhook(self, headers: dict, body: bytes) -> bool:
        pass


    from abc import ABC, abstractmethod

class PaymentProvider(ABC):
    @abstractmethod
    async def charge(self, amount: float, currency: str, source: str):
        pass

    @abstractmethod
    async def verify(self, reference: str):
        pass
