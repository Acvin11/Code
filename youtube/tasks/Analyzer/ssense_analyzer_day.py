import os
import re
import glob
from datetime import datetime
import smtplib
import imghdr
from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from email.message import EmailMessage
from datetime import date, timedelta

today = date.today()

print("Acvin")

HOST = 'smtp.gmail.com'
PORT = 465
EMAIL_ADDRESS = 'rap41120@gmail.com'
EMAIL_PASSWORD = '*par41120'
RECIPENT = 'acvingonsalves@gmail.com'




now = datetime.now()

dt_string = now.strftime("%Y-%m-%d")

content = {}

try:
    for file_name in glob.glob("logger/logger_mail*"):
        #print("Processing file:", file_name)
        log_file = open(file_name, "r")
        file_name = re.sub(r'.*/', '', file_name)
        if "log." in file_name:
            continue
        content[file_name] = log_file.readlines()
        print("Length of content:", len(content[file_name]), file_name)

except:
  print("An exception occurred")

message = ""
for key in content.keys():
    items_generated_through_item_lists = []
    items_actually_updated_through_item_lists = []
    items_failed_to_update_through_items_lists = []
    newly_added_mongos = []
    item_lists = []


    for line in content[key]:
        line = line.strip()
        if dt_string in line:

            urls = re.findall("Product URL through Itemlist : (.*)", line)
            if len(urls) > 0:
                url = str(urls[0])
                url = re.sub("\s.*", "", url)
                items_generated_through_item_lists.append(url)

            urls = re.findall("Pushing newly added item inside priority cache and mongoId is : (.*)", line)
            if len(urls) > 0:
                url = str(urls[0])
                newly_added_mongos.append(url)

            urls = re.findall("DEBUG GET item_lists via .*?:.*?: (.*)", line)
            if len(urls) > 0:
                url = str(urls[0])
                item_lists.append(url)


            urls = re.findall("DEBUG Update item (.*?\\s+)", line)
            if len(urls) > 0:
                url = str(urls[0])
                items_actually_updated_through_item_lists.append(url)

            urls = re.findall("update item with zero price.*?: (.*)", line)
            if len(urls) > 0:
                url = str(urls[0])
                items_failed_to_update_through_items_lists.append(url)



    total_items_added = str(len(newly_added_mongos))
    total_item_lists = str(len(item_lists))
    unique_items_lists = str(len(set(item_lists)))
    total_items_generated_through_item_lists = str(len(items_generated_through_item_lists))
    unique_items_generated_through_item_lists = str(len(set(items_generated_through_item_lists)))
    total_items_actually_updated_through_item_lists = str(len(items_actually_updated_through_item_lists))
    unique_items_actually_update_through_items_lists = str(len(set(items_actually_updated_through_item_lists)))
    total_items_failed_update_through_item_lists = str(len(items_failed_to_update_through_items_lists))
    unique_items_failed_update_through_item_lists = str(len(set(items_failed_to_update_through_items_lists)))


    a = "\nDate: " + dt_string
    b = "\nLog File Name : " + key
    c = "\nItems added :  " + total_items_added
    d = "\nTotal item lists : " + total_item_lists
    e = "\nUnique item lists : " + unique_items_lists
    f = "\nTotal items generated through item lists : " + total_items_generated_through_item_lists
    g = "\nUnique items generated through item lists : " + unique_items_generated_through_item_lists
    h = "\nTotal items actually updated through item lists : " + total_items_actually_updated_through_item_lists
    i = "\nUnique items actually updated through item lists : " + unique_items_actually_update_through_items_lists
    j = "\nTotal items failed to update through item lists : " + total_items_failed_update_through_item_lists
    k = "\nUnique items failed to update through item lists : " + unique_items_failed_update_through_item_lists + "\n\n"


print(message)
comments= str(message)
    


#code
SUBJECT = "Creatively Mix: " + str(today) +" Logger mail" 
msg = EmailMessage()
msg['Subject'] = SUBJECT
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECIPENT


html_page = "<!DOCTYPE html>\n<html><body><h3> "+SUBJECT+"</h3>"

html_page += "<table border = 0 cellpadding = 5>"
fieldnames = [a, b, c, d, e, f, g, h, i, j, k ]

fieldnames = ["\n<tr><td>" + x + "</td></tr>" for x in fieldnames]
html_page +=  " ".join(fieldnames) 
html_page += "\n</body></table></html>"

msg.add_alternative(html_page, subtype='html')
#html_page = """\<!DOCTYPE html><html><bdy><h3 style="color:SlateGray;">"""
#html_page += message
#html_page += """"\</body></html>"""
print(html_page)

msg.add_alternative(html_page, subtype='html')    
   
with smtplib.SMTP_SSL( HOST, PORT) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)


