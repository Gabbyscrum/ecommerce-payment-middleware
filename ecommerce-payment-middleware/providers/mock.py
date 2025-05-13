from app.providers.base import PaymentProvider
import uuid

class MockProvider(PaymentProvider):

    def charge(self, payload):
        return {
            "provider": "mock",
            "payment_id": str(uuid.uuid4()),
            "status": "success",
            "amount": payload["amount"],
            "currency": payload["currency"]
        }

    def verify_webhook(self, headers, body):
        return True
