import pytest

from bank_transfer_qr import QR


@pytest.mark.parametrize(
    argnames='iban,recipient_name,payment_title',
    argvalues=[
        ()
    ]
)
def test_can_create_qr_instance_with_minimal_set_of_parameters(
        iban,
        recipient_name,
        payment_title):
    qr = QR(
        iban=iban,
        recipient_name=recipient_name,
        payment_title=payment_title
    )
    assert isinstance(qr, QR)


def test_can_create_qr_instance_with_all_parameters(
        recipient_identifier,
        country_code,
        iban,
        amount,
        recipient_name,
        payment_title):
    qr = QR(
        iban=iban,
        recipient_name=recipient_name,
        recipient_identifier=recipient_identifier,
        country_code=country_code,
        amount=amount,
        payment_title=payment_title
    )
    assert isinstance(qr, QR)


def test_qr_text_format_of_qr_instance():
    pass


def test_can_save_code_to_file():
    pass


def test_raises_value_error_when_save_directory_not_exists():
    pass

