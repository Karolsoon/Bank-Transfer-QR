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

    def _validate_one(self, value: str, definition: dict, field_name: str):
        validation_exception = definition['validation_exception']
        validator = definition['validator']
        if not validator.search(value):
            raise validation_exception(f'Incorrect {field_name} format')

    def _transform(self, **kwargs):
        for field_name, value in kwargs.items():
            transformed = self._transform_one(
                field_name=field_name,
                value=value
            )
            # TODO: UGLY, not readable.
            self.__setattr__(field_name,transformed)

    def _transform_one(
            self,
            field_name: str,
            value: str|int|float
            ) -> str:
        definition = self.__get_definition(field_name)
        transformations = self.__get_transformations(definition)
        self.__validate_transformations_are_callable(
            transformations,
            field_name
        )
        self.__validate_input_type(value, definition, field_name)
        item = value
        for t in transformations:
            func, args = t
            item = func(item, *args)
        return item

    def __validate_transformations_are_callable(
            self,
            transformations: list[tuple[callable, tuple[str|int|None]]],
            field_name: str):
        for t in transformations:
            if not callable(t[0]):
                raise TypeError(
                    'Transformation must be callable. '
                    f'Please review transformations for "{field_name}"'
                )

    def __validate_input_type(
            self,
            input_value,
            definition: dict,
            field_name: str):
        in_typ = definition['input_types']
        if not isinstance(input_value, in_typ):
            msg = (
                f'"{field_name}" value must be one of {in_typ}, '
                f'not {input_value.__class__.__name__}'
            )
            raise TypeError(msg)

    def __get_definition(self, field_name: str):
        if definition := self.definitions.get(field_name):
            return definition
        raise AttributeError(
            f'Unknown parameter passed into constructor: {field_name}')

    def __get_transformations(self, definition: dict):
        return definition.get('transformations')
