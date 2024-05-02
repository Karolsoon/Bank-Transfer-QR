import re

from src import validators

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


SEPARATOR = '|' # Not negiotiable?


RECIPIENT_IDENTIFIER = {
        'type_1': {
            'required': True,
            'validator': re.compile(
                r'''
                (
                    ^16\d{3} # Optional for systems that operate with 12 digit NIPs
                    |   
                    ^\d{3}     # 3 digits from the NIP
                )
                (-)?    # Separator, optional
                (\d{3}) # 3 digits from the NIP
                (-)?    # Separator, optional
                (\d{2}) # 2 digits from the NIP
                (-)?    # Separator, optional
                (\d{2}) # 2 digits from the NIP
                $
                ''',
                re.VERBOSE),
            'transformations': [
                (str, tuple())
            ],
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
            'transformations': [
                (str, tuple())
            ],
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
    'validator': re.compile(r'^([a-zA-Z]{2})$'),
    'transformations': [
        (str.upper, tuple())
    ],
    'description': 'ISO 3166-2. Two uppercase letters country code'
}


IBAN_PL = {
    'required': True,
    'default': None,
    'validator': re.compile(r'^(PL)?([0-9]{26})$'),
    'transformations': [
        (str, tuple())
    ],
    'description': ('Internatinal Banking Account Number. '
                    'This implementation is specific for Poland.\n'
                    'Other countries may require different validation patterns.\n'
                    'NOTE: Validates only one of the known IBAN formats and '
                    'is nowhere near to inclue the calulation of checksums'
                    ' or other applicable validation steps. ')
}

AMOUNT_IN_POLSKIE_GROSZE = {
    'required': True,
    'default': '000000',
    'validator': re.compile(r'^(\d{6})$'),
    'transformations': [
        (str, tuple()),
        (str.replace, (',', '')),
        (str.replace, ('.', '')),
        (str.rjust, (6, '0'))
    ],
    'description': ('The amount to be transferred to the recipient.\n'
                    'Format is like 9999,00 but without the comma: 999900.\n'
                    'Deviates from the recommendation by NOT allowing higher '
                    'amounts than 9999,99 PLN.')
}


RECIPIENT_NAME = {
    'required': True,
    'default': None,
    'validator': re.compile(r'^([\w -.,/\(\)"\']{3,20})$'),
    'transformations': [
        (str.strip, tuple())
    ],
    'description': ('The name of the recipient. Max. length 20 characters.')
}


PAYMENT_TITLE = {
    'required': True,
    'default': None,
    'validator': re.compile(r'^([\w -.,/\(\)"\']{3,32})$'),
    'transformations': [
        (str.strip, tuple())
    ],
    'description': 'Payment title. Max. length 32 characters.'
}


RESERVE_1 = {
    'required': True,
    'default': '',
    'description': 'Unused.'
}


RESERVE_2 = {
    'required': True,
    'default': '',
    'description': 'Unused.'
}


RESERVE_3 = {
    'required': True,
    'default': '',
    'description': 'Unused.'
}
