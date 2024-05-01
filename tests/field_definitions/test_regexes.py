import re

import pytest

from src.field_definitions import (
    RECIPIENT_IDENTIFIER,
    COUNTRY_CODE,
    IBAN_PL,
    AMOUNT_IN_POLSKIE_GROSZE,
    RECIPIENT_NAME,
    PAYMENT_TITLE
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
