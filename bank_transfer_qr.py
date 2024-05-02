import segno

from src.field_definitions import (
    QR_TEXT_FORMAT,
    RECIPIENT_IDENTIFIER,
    COUNTRY_CODE,
    IBAN_PL,
    AMOUNT_IN_POLSKIE_GROSZE,
    RECIPIENT_NAME,
    TRANSFER_TITLE
)


class QR:

    # QR code requirements
    __encoding = 'UTF-8'
    __error_correction = 'L'
    __min_size_px = {
        'width': 250,
        'height': 250
    }
    __min_size_cm = {
        'width': 1.8,
        'height': 1.8
    }
    __qr_text_format = QR_TEXT_FORMAT

    # Formating requirements and definitions
    definitions = {
        'recipient_identifier': RECIPIENT_IDENTIFIER,
        'country_code': COUNTRY_CODE,
        'iban': IBAN_PL,
        'amount': AMOUNT_IN_POLSKIE_GROSZE,
        'recipient_name': RECIPIENT_NAME,
        'transfer_title': TRANSFER_TITLE
    }

    def __init__(
            self,
            iban: str,
            recipient_name: str,
            transfer_title: str,
            amount: int|str=definitions['amount']['default'],
            country_code: str=definitions['country_code']['default'],
            recipient_identifier: str|int=definitions['recipient_identifier'
                                                  ]['type_2']['default']
            ):
        self.iban = iban
        self.recipient_name = recipient_name
        self.transfer_title = transfer_title
        self.amount = amount
        self.country_code = country_code
        self.recipient_identifier = recipient_identifier

    def make(self, size: dict[str, int|float]) -> None:
        pass

    def _validate(self) -> None:
        pass

    @staticmethod
    def _validate_one(value: str, definition: dict, field_name: str):
        validation_exception = definition['validation_exception']
        validator = definition['validator']
        if not validator.search(value):
            raise validation_exception(f'Incorrect {field_name} format')


    @staticmethod
    def _transform_one(
            value: str|int,
            transformations: list[tuple[callable, tuple]]
            ) -> str:
        pass
