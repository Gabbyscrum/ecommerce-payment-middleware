class PaymentException(Exception):
    pass

class ProviderNotSupported(PaymentException):
    pass

class UnauthorizedException(PaymentException):
    pass
from fastapi import HTTPException

class ProviderError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=502, detail=detail)
