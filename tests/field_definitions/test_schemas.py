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
                'type': list
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
            'type': list,
            'item': {
                'required': False,
                'type': tuple
            }
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

        expected_field_type = exp[field].get('type', object)
        # If the schema has a type tp check
        if isinstance(expected_field_type, type):
            assert isinstance(schema[field], expected_field_type)
            # If the current field is expected to be a list or tuple, unpack the field
            if isinstance(expected_field_type, (tuple, list)):
                was_there_an_item_inside_the_iterable = False
                for item in field:
                    was_there_an_item_inside_the_iterable = True
                    is_item_required = exp[field]['item']['required']
                    # ... check it's type
                    assert isinstance(item, exp[field]['item'].get('type', object))
                # ... if the item is required, check if there was an item
                if is_item_required:
                    assert was_there_an_item_inside_the_iterable == is_item_required
        else:
            assert exp[field]['type'](schema[field])
