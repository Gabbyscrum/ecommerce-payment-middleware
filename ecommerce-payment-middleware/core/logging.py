from abc import ABC, abstractmethod

class PaymentProvider(ABC):

    @abstractmethod
    def charge(self, payload: dict) -> dict:
        pass

    @abstractmethod
    def verify_webhook(self, headers: dict, body: bytes) -> bool:
        pass

    import logging

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO
)

logger = logging.getLogger("middleware")
