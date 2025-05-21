from fastapi import APIRouter, Depends, Header
from app.api.schemas import PaymentRequest
from app.services.payment_service import PaymentService
from app.middleware.auth import api_key_auth
from app.core.idempotency import generate_idempotency_key
from app.storage.memory import InMemoryRepository

router = APIRouter()
service = PaymentService()
repo = InMemoryRepository()

@router.post("/payments")
def create_payment(
    payload: PaymentRequest,
    idempotency_key: str = Header(...),
    _: str = Depends(api_key_auth)
):
    cached = repo.get(idempotency_key)
    if cached:
        return cached

    result = service.process(payload.provider, payload.dict())
    repo.set(idempotency_key, result)
    return result
