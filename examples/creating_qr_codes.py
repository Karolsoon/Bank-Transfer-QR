from bank_transfer_qr import QR


# Get information about the input parameters
QR.info()


# Creating an instance with minimal subset of parameters
qr = QR(
    iban='01234567890123456789012345',
    recipient_name='John Doe',
    transfer_title='Payment title'
)

# Creating a QR instance with all parameters for a non-institutional recipient
qr = QR(
    country_code='PL',
    iban='PL01234567890123456789012345',
    amount='000123',
    recipient_name='Bob Smith',
    transfer_title='Payment title'
)


# Creating an instance for an institutional recipient
qr = QR(
    recipient_identifier='123-123-12-12',
    country_code='PL',
    iban='PL01234567890123456789012345',
    amount='000123',  # Same as 1,23 zł
    recipient_name='My Bank',
    transfer_title='Payment title'
)

# Save the QR code as a file
qr.save('svg_filename', 'svg')
qr.save('png_filename', 'png')


# ...or get an io.BytesIO object and do something with it
qr.get()
qr.get('png')
qr.get('svg')


# Display the QR code instread of writing it anywhere
qr.show()
