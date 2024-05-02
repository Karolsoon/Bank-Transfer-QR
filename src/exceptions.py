# pylint: disable=R0903,C0114


class ValidationError(Exception):
    """
    Base Exception for validation errors that may occur.
    """


class IBANValidationError(ValidationError):
    """
    Raised when the IBAN validation fails. 
    Can be a type, pattern or value validation error.
    """


class RecipientNameValidationError(ValidationError):
    """
    Raised when the Recipient Name validation fails. 
    Can be a type, pattern or value validation error.
    """


class AmountValidationError(ValidationError):
    """
    Raised when the Amount validation fails. 
    Can be a type, pattern or value validation error.
    """


class CountryCodeValidationError(ValidationError):
    """
    Raised when the Country Code validation fails. 
    Can be a type, pattern or value validation error.
    """


class TransferTitleValidationError(ValidationError):
    """
    Raised when the Transfer Title validation fails. 
    Can be a type, pattern or value validation error.
    """


class RecipientIdentifierValidationError(ValidationError):
    """
    Raised when the Recipient Identifier validation fails. 
    Can be a type, pattern or value validation error.
    """
