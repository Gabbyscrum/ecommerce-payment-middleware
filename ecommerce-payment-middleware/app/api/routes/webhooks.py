from fastapi import APIRouter, Request
from app.services.webhook_service import WebhookService

router = APIRouter()
service = WebhookService()

@router.post("/webhooks/stripe")
async def stripe_webhook(request: Request):
    body = await request.body()
    valid = service.handle_stripe(request.headers, body)

    return {"status": "ok" if valid else "invalid"}
