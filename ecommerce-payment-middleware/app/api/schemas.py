from pydantic import BaseModel, Field

class PaymentRequest(BaseModel):
    provider: str
    amount: int = Field(gt=0)
    currency: str
    payment_method: str | None = None

class PaymentResponse(BaseModel):
    provider: str
    payment_id: str
    status: str
    amount: int
    currency: str
