import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
import subprocess
import sys
import pandas as pd
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

timehrstr = datetime.now()
timehr = int(timehrstr.strftime("%I"))
timeDay = timehrstr.strftime("%a")
if (timehr < 9 and timeDay != "Sat" and timeDay != "Sun"):
	sheet = client.open("unittest").worksheet("dailytask1stshift")
elif (timehr > 9):
	sheet = client.open("unittest").worksheet("dailytask2ndshift")
else:
	sys.exit()

data = sheet.get_all_records()

devtask = "/tmp/devtask.txt"
with open(devtask, 'w') as csvfile:
	for person in data:
		for key in person:
			task = person[key]
			csvfile.write(task + "\n")

dateTimeObj = datetime.now()
timestampStr = dateTimeObj.strftime("%d-%b-%Y")
email = "rap41120@gmail.com"
if (timehr < 9):
	command = 'cat "{}" | mutt -s "Task for development team members of 1st shift {}" -- "{}"'.format(devtask, timestampStr, email)
	a = subprocess.Popen(command, shell=True)
	a.communicate()
else:
	command = 'cat "{}" | mutt -s "Task for development team members of 2nd shift {}" -- "{}"'.format(devtask, timestampStr, email)
	a = subprocess.Popen(command, shell=True)
	a.communicate()

sheet.clear()


"""

def send_email(subject, message, to_email):
    # Email configurations
    smtp_server = 'smtp.gmail.com'  # Change this to your SMTP server if not using Gmail
    smtp_port = 587  # Change this to your SMTP port if different

    # Your email credentials
    sender_email = 'your_email@gmail.com'  # Change this to your email address
    sender_password = 'your_password'  # Change this to your email password

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add message body
    msg.attach(MIMEText(message, 'plain'))

    # Create SMTP session for sending the mail
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)  # Login
        server.sendmail(sender_email, to_email, msg.as_string())  # Send email
        print("Email sent successfully to", to_email)

def dailyTask():
    try:
        # Define file location and credentials file
        if os.name == "posix":  # Linux
            fileLocation = '/tmp/'
        elif os.name == "nt":  # Windows
            fileLocation = 'D:\\softwares\\jupyter_notebook\\my_code\\tasks\\'
        else:
            raise OSError("Unsupported operating system.")

        credsFile = fileLocation + "cred_Json/creds.json"

        # Define the name of your Google Spreadsheet
        spreadsheetName = 'Acvin'

        # Authenticate with Google Sheets
        scope = ["https://spreadsheets.google.com/feeds",
                 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]

        creds = Credentials.from_service_account_file(credsFile, scopes=scope)
        client = gspread.authorize(creds)

        # Open the Google Spreadsheet
        spreadsheet = client.open(spreadsheetName)

        currentTime = datetime.now()
        hour = int(currentTime.strftime("%H"))  # Use 24-hour format for simplicity
        day = currentTime.strftime("%a")

        # Determine the worksheet based on current time
        if 9 <= hour < 17 and day not in ["Sat", "Sun"]:
            sheet = client.open(spreadsheetName).worksheet("dailytask1stshift")
        elif hour >= 17:
            sheet = client.open(spreadsheetName).worksheet("dailytask2ndshift")
        else:
            sys.exit()

        data = sheet.get_all_records()  # Get a list of all records in the worksheet
        df = pd.DataFrame.from_dict(data)
        print(df)

        # Determine the appropriate path for the temporary task file based on the operating system
        devTask = os.path.join(fileLocation, "devtask.txt")

        # Write tasks to the temporary file
        with open(devTask, 'w') as csvfile:
            for person in data:
                for key in person:
                    task = person[key]
                    csvfile.write(task + "\n")

        # Get current date for email subject
        timestampStr = currentTime.strftime("%d-%b-%Y")
        email = "rap41120@gmail.com"

        # Compose email subject based on shift
        shift = "1st" if 9 <= hour < 17 else "2nd"

        # Compose email message
        message = f"Task for development team members of {shift} shift {timestampStr}"

        # Send email
        send_email(message, devTask, email)

        # Clear the worksheet after sending tasks
        sheet.clear()

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    dailyTask()
"""
