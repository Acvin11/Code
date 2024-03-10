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
from datetime import date, timedelta

print("Code execution..")

#Mailer

HOST = 'smtp.gmail.com'
PORT = 465
EMAIL_ADDRESS = 'rap41120@gmail.com'
EMAIL_PASSWORD = 'Acvin1997'
RECIPENT = 'acvingonsalves@gmail.com'#,rap41120@gmail.com,denila347@gmail.com,siddharthkavil23@gmail.com'

today = date.today()

msg = EmailMessage()
SUBJECT = "Creatively Mix: " + str(today) +" Daily Task Mail" 
msg['Subject'] = SUBJECT 
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECIPENT

#Spreadsheet Code
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("cred_Json/creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Acvin").sheet1  # Open the spreadhseet

data = data2= sheet.get_all_records()  # Get a list of all records

records_df = pd.DataFrame.from_dict(data)
pprint(records_df)


#code
html_page = "<!DOCTYPE html>\n<html>"
html_page += '<h4><p><a href="https://docs.google.com/spreadsheets/d/188PjTrLh71VOsQ68UR2GJ8uN22xjnO9iEeks80ft5tE/edit#gid=194942762">https://docs.google.com/spreadsheets/d/188PjTrLh71VOsQ68UR2GJ8uN22xjnO9iEeks80ft5tE/edit#gid=194942762</a></p>'

html_page += "</h4><table style='background-color: grey;' border = 2 cellpadding = 10>"
fieldnames = ["Date", "Category ", "Task  ", "Status", "Assignee", "Comments", "Links"]
fieldnames = ["<th>" + x + "</th>" for x in fieldnames]
html_page += "\n<tr  style='color:white; background-color: black;'> " + " ".join(fieldnames)  + " </tr>"
for document in data:
    category= str(document["Category"])
    dates= str(document["Date"])
    task= str(document["Task"])
    assignee = str(document["Assignee"])
    status= str(document["Status"])
    comments= str(document["Comments"])
    category= str(document["Category"])
    links= str(document["Links"])
    if(category != 'Website' and comments != 'published'):    
            data = [dates, category, task, status, assignee, comments, links]
            data = [x.encode('utf-8').decode('latin-1') for x in data]
            data = ["<td style='color:black; background-color: white;'>" + x + "</td>" for x in data]
            html_page += "\n<tr> " + " ".join(data) + " </tr>"


html_page += "\n</table>"
#print(html_page)
html_page += "<br><br><h3 style='color:green;'> Task Completed !!! </h3> <br>"
html_page += "<table style='background-color: grey;' border = 2 cellpadding = 10>"

fieldnames2 = ["Date", "Category ", "Task  ", "Status", "Assignee", "Comments", "Links"]
fieldnames2 = ["<th>" + x + "</th>" for x in fieldnames2]

html_page += "\n<tr  style='color:white; background-color: black;'> " + " ".join(fieldnames2)  + " </tr>"
for document2 in data2:
    category= str(document2["Category"])
    dates= str(document2["Date"])
    task= str(document2["Task"])
    assignee = str(document2["Assignee"])
    status= str(document2["Status"])
    comments= str(document2["Comments"])
    category= str(document2["Category"])
    links= str(document2["Links"])
    if(category != 'Website' and comments == 'published'):    
        data = [dates, category, task, status, assignee, comments, links]
        data = [x.encode('utf-8').decode('latin-1') for x in data]
        data = ["<td style='color:black; background-color: white;'>" + x + "</td>" for x in data]
        html_page += "\n<tr> " + " ".join(data) + " </tr>"
html_page += "\n</table></html>"    

msg.add_alternative(html_page, subtype='html')


#files = ['attachment/attach.jpg']
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
