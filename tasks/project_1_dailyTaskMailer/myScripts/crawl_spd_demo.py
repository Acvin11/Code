import os
import smtplib
import imghdr
import pandas as pd
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from email.message import EmailMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import csv , time
import requests

print("Code execution..")

#Mailer

HOST = 'smtp.gmail.com'
PORT = 465
EMAIL_ADDRESS = 'rap41120@gmail.com'
EMAIL_PASSWORD = '*par41120'
RECIPENT = 'acvingonsalves@gmail.com'


msg = EmailMessage()
msg['Subject'] = 'Creatively Mix Bot'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECIPENT

#Spreadsheet Code
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Acvin").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

records_df = pd.DataFrame.from_dict(data)
pprint(records_df)



# #code
# html_page = "<!DOCTYPE html>\n<html><table border = 5 cellpadding = 5>"

# fieldnames = ["Host", "Assignee"]
# fieldnames = ["<th>" + x + "</th>" for x in fieldnames]

# html_page += "\n<tr> " + " ".join(fieldnames)  + " </tr>"

# for document in data:
#     host = str(document["Host"])
    
#     assignee = str(document["Assignee"])
#     print(host +" | "+ assignee)
    

#     data = [host, assignee]
#     data = [x.encode('utf-8').decode('latin-1') for x in data]
#     data = ["<td>" + x + "</td>" for x in data]

#     html_page += "\n<tr> " + " ".join(data) + " </tr>"


# html_page += "\n</table></html>"
msg.add_alternative(records_df)


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


print("Code Complete!!")
