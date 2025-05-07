class PaymentException(Exception):
    pass

class ProviderNotSupported(PaymentException):
    pass

class UnauthorizedException(PaymentException):
    pass
