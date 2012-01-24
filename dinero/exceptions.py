class DineroException(Exception):
    pass

class GatewayException(DineroException):
    pass

class PaymentException(DineroException):
    """
    This is how errors are reported when submitting a transaction.
    PaymentException has an `errors` property that stores a list of
    `PaymentError` instances, one for each error that occured. The `in`
    operator is overrided to provide a subclass-like interface, so if `a` is an
    instance of `Foo`, `Foo in PaymentException([a])` will be True.
    """

    def __init__(self, errors=None):
        self.errors = errors or []

    def has(self, error):
        return any(isinstance(i, error) for i in self.errors)

    def __contains__(self, key):
        return self.has(key)

    def __repr__(self):
        return "PaymentException(%r)" % (self.errors,)


class PaymentError(DineroException):
    """
    These exceptions are never actually raised, they always belong to a
    PaymentException.
    """
    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.args[0])

class VerificationError(PaymentError):
    pass

class CVVError(VerificationError):
    pass

class AVSError(VerificationError):
    pass

class CardInvalidError(PaymentError):
    pass

class InvalidAmountError(PaymentError):
    pass

class ExpiryError(PaymentError):
    pass

class CardDeclinedError(PaymentError):
    pass

class DuplicateTransactionError(PaymentError):
    pass