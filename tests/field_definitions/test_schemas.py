import re

import pytest

from src.field_definitions import (
    RECIPIENT_IDENTIFIER,
    COUNTRY_CODE,
    IBAN_PL,
    AMOUNT_IN_POLSKIE_GROSZE
)


@pytest.fixture(scope='session')
def recipient_identifier_schema():
    return {
        'field_name': {
            'required': True,
            'type': dict,
            'fields': {
                'required': {
                    'type': bool,
                    'required': True
                },
                'validator': {
                    'type': re.Pattern,
                    'required': True
                },
                'default': {
                    'required': False,
                }
            },
            'description': {
                'type': str,
                'required': True
            },
            'transformations': {
                'required': False,
                'type': tuple
            }
        }
    }


@pytest.fixture(scope='session')
def field_schema():
    return {                
        'required': {
            'type': bool,
            'required': True
        },
        'validator': {
            'type': re.Pattern,
            'required': True
        },
        'default': {
            'required': False,
            'type': object
        },
        'description': {
            'type': str,
            'required': True
        },
        'transformations': {
            'required': False,
            'type': tuple
        }
    }


@pytest.mark.parametrize(
    argnames='schema,expected',
    argvalues=[
        (COUNTRY_CODE, 'field_schema'),
        (IBAN_PL, 'field_schema'),
        (AMOUNT_IN_POLSKIE_GROSZE, 'field_schema')
    ]
)
def test_standard_field_schemas(schema: dict, expected: dict, request):
    exp = request.getfixturevalue(expected)
    for field in schema:
        print(f'Current field: {field}')
        assert field in exp if exp[field]['required'] else True

        if isinstance(exp[field].get('type'), type):
            assert isinstance(schema[field], exp[field].get('type', object))
        else:
            assert exp[field]['type'](schema[field])
