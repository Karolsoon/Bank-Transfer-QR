import re

import pytest

from bank_transfer_qrcode.field_definitions import (
    RECIPIENT_IDENTIFIER,
    COUNTRY_CODE,
    IBAN_PL,
    AMOUNT_IN_POLSKIE_GROSZE,
    RECIPIENT_NAME,
    TRANSFER_TITLE
)


def get_regex(field: dict) -> re.Pattern:
    # Case for "standard" fields with a flat structure
    if v := field.get('validator'):
        return v
    
    # Case for recipient identifier
    return field['type_1']['validator']



@pytest.mark.parametrize(
    argnames='nip',
    argvalues=[
        '123-123-12-12',
        '1231231212',
        '161231231212',
        '16123-123-12-12',
        '16123-123-1212'
    ]
)
def test_correct_recipient_identifier_passes(nip):
    r = get_regex(RECIPIENT_IDENTIFIER)
    result = r.search(nip)
    assert result is not None


@pytest.mark.parametrize(
    argnames='nip',
    argvalues=[
        '123-123-12-1',
        '123123121',
        '11231231212',
        '1612-123-12-12',
        '123-12-1212'
    ]
)
def test_too_short_recipient_identifier_fails(nip):
    r = get_regex(RECIPIENT_IDENTIFIER)
    result = r.search(nip)
    assert result is None


@pytest.mark.parametrize(
    argnames='code',
    argvalues=[
        'pl',
        'PL',
        'de',
        'DE',
        'GB',
        'pL',
        'Pl'
    ]
)
def test_correct_country_code_passes(code):
    r = get_regex(COUNTRY_CODE)
    result = r.search(code)
    assert result is not None


@pytest.mark.parametrize(
    argnames='code',
    argvalues=[
        'POL',
        'pol',
        'PoL',
        'P',
        'p1',
        '16',
        '\\w',
        '\\w*',
        ''
    ]
)
def test_incorrect_country_code_fails(code):
    r = get_regex(COUNTRY_CODE)
    result = r.search(code)
    assert result is None


@pytest.mark.parametrize(
    argnames='iban',
    argvalues=[
        'PL01234567890123456789012345',
        '01234567890123456789012345'
    ]
)
def test_correct_iban_passes(iban):
    r = get_regex(IBAN_PL)
    result = r.search(iban)
    assert result is not None


@pytest.mark.parametrize(
    argnames='iban',
    argvalues=[
        'PL01 2345 6789 0123 4567 8901 2345',
        '0123 4567 8901 2345 6789 0123 45',
        'pl12123412341234123412341234'
    ]
)
def test_incorrect_iban_format_fails(iban):
    r = get_regex(IBAN_PL)
    result = r.search(iban)
    assert result is None


@pytest.mark.parametrize(
    argnames='iban',
    argvalues=[
        'PL0123456789012345678901234',
        'PL012345678901234567890123451',
        '1234567890123456789012345'
    ]
)
def test_incorrect_iban_length_fails(iban):
    r = get_regex(IBAN_PL)
    result = r.search(iban)
    assert result is None


@pytest.mark.parametrize(
    argnames='recipient',
    argvalues=[
        'Paweł Sokół',
        'Krzywy Zgryz 6',
        'ASG Polska Sp.z o.o.',
        'Firma (Global)',
        'Hurt-Detal Sp.z o.o.',
        'Sedlak/Sedlak',
        '8-Bit "PHU-Janusz"',
        """ąęźłóóććśśś ',"()/"""
    ]
)
def test_correct_recipient_name_passes(recipient):
    r = get_regex(RECIPIENT_NAME)
    result = r.search(recipient)
    assert result is not None


@pytest.mark.parametrize(
    argnames='recipient',
    argvalues=[
        '123456789012345678901'
    ]
)
def test_too_long_recipient_name_fails(recipient):
    r = get_regex(RECIPIENT_NAME)
    result = r.search(recipient)
    assert result is None


@pytest.mark.parametrize(
    argnames='recipient',
    argvalues=[
        '12'
    ]
)
def test_too_short_recipient_name_fails(recipient):
    r = get_regex(RECIPIENT_NAME)
    result = r.search(recipient)
    assert result is None


@pytest.mark.parametrize(
    argnames='TRANSFER_title',
    argvalues=[
        '01234567890123456789012345678901',     # 32 characters
        'Dziękuję za przelew',
        'FV20241110123',
        'FV2024/11/10/123',
        'FV 2024/11/10/123',
        'FV 2024/11/10-123',
        'Firma (Poland) FV1234',
        'Dzi',
        """ąęźłóóććśśś ',"()/ blablablabl"""
    ]
)
def test_correct_TRANSFER_title_passes(TRANSFER_title):
    r = get_regex(TRANSFER_TITLE)
    result = r.search(TRANSFER_title)
    assert result is not None


@pytest.mark.parametrize(
    argnames='TRANSFER_title',
    argvalues=[
        '012345678901234567890123456789012'     # 33 characters
    ]
)
def test_too_long_TRANSFER_title_fails(TRANSFER_title):
    r = get_regex(TRANSFER_TITLE)
    result = r.search(TRANSFER_title)
    assert result is None


@pytest.mark.parametrize(
    argnames='TRANSFER_title',
    argvalues=[
        'Dz'
    ]
)
def test_too_short_TRANSFER_title_fails(TRANSFER_title):
    r = get_regex(TRANSFER_TITLE)
    result = r.search(TRANSFER_title)
    assert result is None


@pytest.mark.parametrize(
    argnames='amount_in_polskie_grosze',
    argvalues=[
        '123456',
        '000100',
        '019999',
        '000000'
    ]
)
def test_correct_amount_in_polskie_grosze_passes(amount_in_polskie_grosze):
    r = get_regex(AMOUNT_IN_POLSKIE_GROSZE)
    result = r.search(amount_in_polskie_grosze)
    assert result is not None


@pytest.mark.parametrize(
    argnames='amount_in_polskie_grosze',
    argvalues=[
        '123,11',
        '123.11',
        '123PLN',
        '123 zł',
        '123,11 zł',
        '123 11'
    ]
)
def test_wrong_forma_amount_in_polskie_grosze_fails(amount_in_polskie_grosze):
    r = get_regex(AMOUNT_IN_POLSKIE_GROSZE)
    result = r.search(amount_in_polskie_grosze)
    assert result is None
