import pytest

from bank_transfer_qrcode.field_definitions import (
    RECIPIENT_IDENTIFIER,
    COUNTRY_CODE,
    IBAN_PL,
    AMOUNT_IN_POLSKIE_GROSZE,
    RECIPIENT_NAME,
    TRANSFER_TITLE
)


@pytest.mark.parametrize(
        argnames='input_value,expected',
        argvalues=[
            ('123-123-12-12', '123-123-12-12'),
            (1231231212, '1231231212'),
            ('    1231231212', '1231231212'),
            ('   123   123 12-12', '12312312-12')
        ]
)
def test_recipient_identifier_transformation_is_executable(input_value, expected):
    transformations = RECIPIENT_IDENTIFIER['type_2']['transformations']
    s = input_value
    for t in transformations:
        func, args = t
        s = func(s, *args)
    assert s == expected


@pytest.mark.parametrize(
        argnames='input_value,expected',
        argvalues=[
            (' pl  ', 'PL'),
            ('pL   ', 'PL'),
            ('\n\np6     ', 'P6')
        ]
)
def test_country_code_transformation_is_executable(input_value, expected):
    transformations = COUNTRY_CODE['transformations']
    s = input_value
    for t in transformations:
        func, args = t
        s = func(s, *args)
    assert s == expected


@pytest.mark.parametrize(
        argnames='input_value,expected',
        argvalues=[
            ('PL01234567890123456789012345', 'PL01234567890123456789012345'),
            (1234567890123456789012345, '1234567890123456789012345'),
            (' PL01234567890123456789012345   ', 'PL01234567890123456789012345')

        ]
)
def test_iban_transformation_is_executable(input_value, expected):
    transformations = IBAN_PL['transformations']
    s = input_value
    for t in transformations:
        func, args = t
        s = func(s, *args)
    assert s == expected


@pytest.mark.parametrize(
        argnames='input_value,expected',
        argvalues=[
            (1000, '001000'),
            ('11,22', '001122'),
            ('1000', '001000'),
            ('333,44', '033344'),
            ('555.66', '055566'),
            (777.88, '077788'),
            ('0', '000000'),
            (0, '000000'),
            (0.0, '000000'),
            ('  1111    ', '001111')
        ]
)
def test_amount_transformation_is_executable(input_value, expected):
    transformations = AMOUNT_IN_POLSKIE_GROSZE['transformations']
    s = input_value
    for t in transformations:
        func, args = t
        s = func(s, *args)
    assert s == expected


@pytest.mark.parametrize(
        argnames='input_value,expected',
        argvalues=[
            ('  Bob    Smith', 'Bob Smith'),
            ('\nBob   Smith\n  ', 'Bob Smith'),
            ('BobSmith\n\n', 'BobSmith')
        ]
)
def test_recipient_name_transformation_is_executable(input_value, expected):
    transformations = RECIPIENT_NAME['transformations']
    s = input_value
    for t in transformations:
        func, args = t
        s = func(s, *args)
    assert s == expected


@pytest.mark.parametrize(
        argnames='input_value,expected',
        argvalues=[
            ('Payment    title ', 'Payment title'),
            ('\nPayment        title', 'Payment title'),
            ('     Payment\n\ntitle\t\t', 'Payment title')
        ]
)
def test_transfer_title_transformation_is_executable(input_value, expected):
    transformations = TRANSFER_TITLE['transformations']
    s = input_value
    for t in transformations:
        func, args = t
        s = func(s, *args)
    assert s == expected
