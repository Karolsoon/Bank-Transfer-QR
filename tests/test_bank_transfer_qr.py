import pytest

from bank_transfer_qr import QR
from src.exceptions import ValidationError
from src.field_definitions import (
    RECIPIENT_IDENTIFIER,
    COUNTRY_CODE,
    IBAN_PL,
    AMOUNT_IN_POLSKIE_GROSZE,
    RECIPIENT_NAME,
    TRANSFER_TITLE
)


@pytest.fixture(scope='function')
def qr_instance():
    return QR(
        iban='01234567890123456789012345',
        recipient_name='John Doe',
        transfer_title='Payment title'
    )


@pytest.mark.parametrize(
    argnames='iban,recipient_name,payment_title',
    argvalues=[
        ('1234567890123456789012345', 'Bob Smith', 'Payment title'),
        ('1234567890123456789012345', 'Bob ąąąśśśććććłłłóóó', 'Payment tłłóśąęć'),
        ('PL1234567890123456789012345', 'Bob Smith', 'Payment title')
    ]
)
def test_can_create_qr_instance_with_minimal_set_of_parameters(
        iban,
        recipient_name,
        payment_title):
    qr = QR(
        iban=iban,
        recipient_name=recipient_name,
        transfer_title=payment_title
    )
    assert isinstance(qr, QR)


def test_can_create_qr_instance_with_all_parameters():
    recipient_identifier = '123-123-12-12'
    country_code = 'PL'
    iban = 'PL1234567890123456789012345'
    amount = '000123'
    recipient_name = 'Bob Smith'
    transfer_title = 'Payment title'
    qr = QR(
        iban=iban,
        recipient_name=recipient_name,
        transfer_title=transfer_title,
        amount=amount,
        recipient_identifier=recipient_identifier,
        country_code=country_code
    )
    assert isinstance(qr, QR)


@pytest.mark.parametrize(
    argnames='value,definition',
    argvalues=[
        ('123-123-12-12', RECIPIENT_IDENTIFIER),
        ('PL01234567890123456789012345', IBAN_PL),
        ('PL', COUNTRY_CODE),
        ('Bob Smith', RECIPIENT_NAME),
        ('000123', AMOUNT_IN_POLSKIE_GROSZE),
        ('FV 2024/11/12-0006', TRANSFER_TITLE)
    ]
)
def test_validate_one_method_correctly_uses_arguments(
        value: str,
        definition: dict,
        qr_instance: QR):
    try:
        qr_instance._validate_one(value, definition)
    except ValidationError:
        pytest.fail('Validation in _validate_one() failed but should pass')
    except Exception:
        pytest.fail('An exception was raised while processing _validate_one()')    


@pytest.mark.parametrize(
    argnames='value,definition',
    argvalues=[
        ('123-123-12-12', RECIPIENT_IDENTIFIER),
        ('PL01234567890123456789012345', IBAN_PL),
        ('PL', COUNTRY_CODE),
        ('Bob Smith', RECIPIENT_NAME),
        ('000123', AMOUNT_IN_POLSKIE_GROSZE),
        ('FV 2024/11/12-0006', TRANSFER_TITLE)
    ]
)
def test_validate_one_raises_relevant_validation_error_when_validation_failed(
        value,
        definition,
        qr_instance):
    pass


def test_qr_text_format_of_qr_instance():
    pass


def test_can_save_code_to_file():
    pass


def test_raises_value_error_when_save_directory_not_exists():
    pass

