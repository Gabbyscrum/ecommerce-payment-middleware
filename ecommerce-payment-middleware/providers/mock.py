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
    from fastapi import APIRouter
from app.providers import get_provider

router = APIRouter(prefix="/payments")

@router.post("/charge")
async def charge(payload: dict):
    provider = get_provider(payload.get("provider"))
    return await provider.charge(
        payload["amount"], payload["currency"], payload["source"]
    )
