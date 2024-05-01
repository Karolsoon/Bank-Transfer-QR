import re


QR_TEXT_FORMAT = ('{recipient_identifier}'
            '{separator}'
            '{country_code}'
            '{separator}'
            '{IBAN}'
            '{separator}'
            '{amount_in_polskie_grosze}'
            '{separator}'
            '{recipient_name}'
            '{separator}'
            '{payment_title}'
            '{separator}'
            '{reserved_1}'
            '{separator}'
            '{reserved_2}'
            '{separator}'
            '{reserved_3}'
)


RECIPIENT_IDENTIFIER = {
        'type_1': {
            'required': True,
            'validator': re.compile(
                r'''
                ^
                (16)?   # Optional for systems that operate with 12 digit NIPs
                (\d{3}) # 3 digits from the NIP
                (-)?    # Separator, optional
                (\d{3}) # 3 digits from the NIP
                (-)?    # Separator, optional
                (\d{2}) # 2 digits from the NIP
                (-)?    # Separator, optional
                (\d{2}) # 2 digits from the NIP
                ''',
                re.VERBOSE),
            'transformation': str,
            'default': None
        },
        'type_2': {
            'required': False,
            'validator': re.compile( # Only relevant if provided, can be empty
                r'''
                ^
                (16)?   # Optional for systems that operate with 12 digit NIPs
                (\d{3}) # 3 digits from the NIP
                (-)?    # Separator, optional
                (\d{3}) # 3 digits from the NIP
                (-)?    # Separator, optional
                (\d{2}) # 2 digits from the NIP
                (-)?    # Separator, optional
                (\d{2}) # 2 digits from the NIP
                ''',
                re.VERBOSE),
            'transformation': str,
            'default': ''
        },
        'description': ('Recipient identifier.\n'
                        'Type 1: Institutional recipient,\n'
                        'Type 2: Individual recipient (Non-Institutional).\n\n'
                        'Value is always the NIP of the recipient.\n'
                        'Mandatory for type 1 recipients.\n'
                        'Optional for type 2 recipients and can be left empty.')
}
RECIPIENT_IDENTIFIER['default'] = RECIPIENT_IDENTIFIER['type_2']


COUNTRY_CODE = {
    'required': False,
    'default': 'PL',
    'validator': re.compile(r'([A-Z]{2})'),
    'transformation': str.upper,
    'description': 'ISO 3166-2. Two uppercase letters country code'
}

IBAN = {
    'required': True,
    'default': None,
    'validator': re.compile(r'^(PL)?([0-9]{26})'),
    'transformation': str,
    'description': ('Internatinal Banking Account Number. '
                    'This implementation is specific for Poland.\n'
                    'Other countries may require different validation patterns.\n'
                    'NOTE: Validates only one of the known IBAN formats and '
                    'is nowhere near to inclue the calulation of checksums'
                    ' or other applicable validation steps. '),
}

AMOUNT_IN_POLSKIE_GROSZE = {
    'required': True,
    'default': '000000',
    'validator': re.compile(r'^(\d{6})$'),
    'transformation': str,
    'description': ('The amount to be transferred to the recipient.\n'
                    'Format is like 9999,00 but without the comma: 999900.\n'
                    'Deviates from the recommendation by NOT allowing higher '
                    'amounts than 9999,99 PLN.')
}


### TEMPLATE
"""
{
    'required':,
    'default':,
    'validator':,
    'transformation':,
    'description':,
}
"""