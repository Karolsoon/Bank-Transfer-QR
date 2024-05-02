import segno

from src.field_definitions import (
    QR_TEXT_FORMAT,
    RECIPIENT_IDENTIFIER,
    COUNTRY_CODE,
    IBAN_PL,
    AMOUNT_IN_POLSKIE_GROSZE
)

class QR:

    # QR code requirements
    encoding = 'UTF-8'
    error_correction = 'L'
    min_size_px = {
        'width': 250,
        'height': 250
    }
    min_size_cm = {
        'width': 1.8,
        'height': 1.8
    }

    # Formating requirements
    qr_format = QR_TEXT_FORMAT
    recipient_identifier = RECIPIENT_IDENTIFIER
    country_code = COUNTRY_CODE
    iban = IBAN_PL
    amount = AMOUNT_IN_POLSKIE_GROSZE

    def __init__(self):
        ...

    def make(self, size: dict[str, int|float]) -> None:
        ...


