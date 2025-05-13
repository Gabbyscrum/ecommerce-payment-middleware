import stripe
from app.providers.base import PaymentProvider
from app.core.config import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

class StripeProvider(PaymentProvider):

    def charge(self, payload):
        intent = stripe.PaymentIntent.create(
            amount=payload["amount"],
            currency=payload["currency"],
            payment_method=payload["payment_method"],
            confirm=True,
        )

        return {
            "provider": "stripe",
            "payment_id": intent.id,
            "status": intent.status,
            "amount": intent.amount,
        }

    def verify_webhook(self, headers, body):
        try:
            stripe.Webhook.construct_event(
                body,
                headers.get("stripe-signature"),
                settings.STRIPE_WEBHOOK_SECRET
            )
            return True
        except Exception:
            return False
