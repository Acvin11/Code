import os
import smtplib
import imghdr
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from email.message import EmailMessage

print("Acvin")

HOST = 'smtp.gmail.com'
PORT = 465
EMAIL_ADDRESS = 'rap41120@gmail.com'
EMAIL_PASSWORD = '*par41120'
RECIPENT = 'siddharthkavil23@gmail.com'


msg = EmailMessage()
msg['Subject'] = 'Creatively Mix Bot'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECIPENT

 
msg.set_content('Please check ur  work ')

msg.add_alternative("""\
<!DOCTYPE html>
<html>
    <body>
        <h3 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""", subtype='html')


files = ['attach.jpg']
for file in files:
    with open(file, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data, maintype=
                       'image', subtype=file_type, filename=file_name)
    
   
with smtplib.SMTP_SSL( HOST, PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
