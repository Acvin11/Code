import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = 'rap41120@gmail.com'
EMAIL_PASSWORD = 'Acvin1997'
EMAIL_SMTP_SERVER = 'smtp.gmail.com'
EMAIL_SMTP_PORT = 465

contacts = ['acvingonsalves@email.com']

msg = EmailMessage()
msg['Subject'] = 'Please Find My Resume Attached'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'acvingonsalves@gmail.com,rap41120@gmail.com'
msg.set_content('File(s) attached...')

files = ['attach.jpg']

for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        # remove if not an image
        # file_type = imghdr.what(f.name)
        file_name = f.name

    # Image Attachment
    # msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    # PDF Attachment etc.
    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL(EMAIL_SMTP_SERVER, EMAIL_SMTP_PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
    print("Code Complete!!")
print("Code Complete!!")

