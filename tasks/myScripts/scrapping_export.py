import re
import glob
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


now = datetime.now()
dt_string = now.strftime("%Y-%m-%d")
content = {}

try:
    for file_name in glob.glob("/home/admin/website_name_*"):
        #print("Processing file:", file_name)
        log_file = open(file_name, "r")
        file_name = re.sub(r'.*/', '', file_name)
        if "log." in file_name:
            continue
        content[file_name] = log_file.readlines()
        print("Length of content:", len(content[file_name]), file_name)

except:
  print("An exception occurred")

msg = ""
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

            urls = re.findall("Pushing newly added item inside priority cache and Id is : (.*)", line)
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


    msg += "\nDate: " + dt_string
    msg += "\nLog File Name : " + key
    msg += "\nItems added: " + total_items_added
    msg += "\nTotal item lists: " + total_item_lists
    msg += "\nUnique item lists: " + unique_items_lists
    msg += "\nTotal items generated through item lists: " + total_items_generated_through_item_lists
    msg += "\nUnique items generated through item lists: " + unique_items_generated_through_item_lists
    msg += "\nTotal items actually updated through item lists: " + total_items_actually_updated_through_item_lists
    msg += "\nUnique items actually updated through item lists: " + unique_items_actually_update_through_items_lists
    msg += "\nTotal items failed to update through item lists: " + total_items_failed_update_through_item_lists
    msg += "\nUnique items failed to update through item lists: " + unique_items_failed_update_through_item_lists + "\n\n"


print(msg)

email = "rap41120@gmail.com"


subject = "All export for the day"

command = 'echo "{}" | mutt  {} -s "{}"'.format(msg, email, subject)

os.system(command)

"""


# Get current date
dt_string = datetime.now().strftime("%Y-%m-%d")

content = {}

try:
    # Iterate through log files
    for file_name in glob.glob("/home/admin/website_name_*"):
        if "log." in file_name:
            continue
        with open(file_name, "r") as log_file:
            file_name = os.path.basename(file_name)
            content[file_name] = log_file.readlines()
            print("Length of content:", len(content[file_name]), file_name)

except Exception as e:
    print("An exception occurred:", e)

# Initialize message
msg = ""

for key, lines in content.items():
    # Initialize lists to store data
    items_generated_through_item_lists = []
    newly_added_mongos = []
    item_lists = []
    items_actually_updated_through_item_lists = []
    items_failed_to_update_through_items_lists = []

    for line in lines:
        line = line.strip()
        if dt_string in line:
            urls = re.findall("Product URL through Itemlist : (.*)", line)
            if urls:
                items_generated_through_item_lists.append(urls[0].split()[0])

            urls = re.findall("Pushing newly added item inside priority cache and Id is : (.*)", line)
            if urls:
                newly_added_mongos.append(urls[0])

            urls = re.findall("DEBUG GET item_lists via .*?:.*?: (.*)", line)
            if urls:
                item_lists.append(urls[0])

            urls = re.findall("DEBUG Update item (.*?\\s+)", line)
            if urls:
                items_actually_updated_through_item_lists.append(urls[0])

            urls = re.findall("update item with zero price.*?: (.*)", line)
            if urls:
                items_failed_to_update_through_items_lists.append(urls[0])

    # Calculate statistics
    total_items_added = len(newly_added_mongos)
    total_item_lists = len(item_lists)
    unique_items_lists = len(set(item_lists))
    total_items_generated_through_item_lists = len(items_generated_through_item_lists)
    unique_items_generated_through_item_lists = len(set(items_generated_through_item_lists))
    total_items_actually_updated_through_item_lists = len(items_actually_updated_through_item_lists)
    unique_items_actually_update_through_items_lists = len(set(items_actually_updated_through_item_lists))
    total_items_failed_update_through_item_lists = len(items_failed_to_update_through_items_lists)
    unique_items_failed_update_through_item_lists = len(set(items_failed_to_update_through_items_lists))

    # Construct message
    msg += "\nDate: " + dt_string
    msg += "\nLog File Name : " + key
    msg += "\nItems added: " + str(total_items_added)
    msg += "\nTotal item lists: " + str(total_item_lists)
    msg += "\nUnique item lists: " + str(unique_items_lists)
    msg += "\nTotal items generated through item lists: " + str(total_items_generated_through_item_lists)
    msg += "\nUnique items generated through item lists: " + str(unique_items_generated_through_item_lists)
    msg += "\nTotal items actually updated through item lists: " + str(total_items_actually_updated_through_item_lists)
    msg += "\nUnique items actually updated through item lists: " + str(unique_items_actually_update_through_items_lists)
    msg += "\nTotal items failed to update through item lists: " + str(total_items_failed_update_through_item_lists)
    msg += "\nUnique items failed to update through item lists: " + str(unique_items_failed_update_through_item_lists) + "\n\n"

print(msg)

# Email configurations
smtp_server = 'smtp.gmail.com'  # Change this to your SMTP server if not using Gmail
smtp_port = 587  # Change this to your SMTP port if different
sender_email = 'your_email@gmail.com'  # Change this to your email address
sender_password = 'your_password'  # Change this to your email password
receiver_email = "rap41120@gmail.com"
subject = "All export for the day"

# Create message container
email_msg = MIMEMultipart()
email_msg['From'] = sender_email
email_msg['To'] = receiver_email
email_msg['Subject'] = subject

# Add message body
email_msg.attach(MIMEText(msg, 'plain'))

# Create SMTP session for sending the mail
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Secure the connection
    server.login(sender_email, sender_password)  # Login
    server.sendmail(sender_email, receiver_email, email_msg.as_string())  # Send email
    print("Email sent successfully to", receiver_email)
"""
