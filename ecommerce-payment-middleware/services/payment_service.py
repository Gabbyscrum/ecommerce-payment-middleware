from app.providers.mock import MockProvider
from app.providers.stripe import StripeProvider
from app.core.exceptions import ProviderNotSupported

PROVIDERS = {
    "mock": MockProvider(),
    "stripe": StripeProvider(),
}

class PaymentService:

    def process(self, provider: str, payload: dict) -> dict:
        if provider not in PROVIDERS:
            raise ProviderNotSupported(f"{provider} not supported")

        return PROVIDERS[provider].charge(payload)
