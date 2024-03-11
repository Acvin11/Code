import pandas as pd
import gspread
from google.oauth2.service_account import Credentials

# Define the common path to the file location
file_location = 'D:\\softwares\\jupyter_notebook\\my_code\\tasks\\'

def writing_to_google_spreadsheet(df, spreadsheet_name, worksheet_name):
    try:
        # Authenticate with Google Sheets
        scope = ["https://spreadsheets.google.com/feeds",
                 'https://www.googleapis.com/auth/spreadsheets',
                 "https://www.googleapis.com/auth/drive.file",
                 "https://www.googleapis.com/auth/drive"]

        creds = Credentials.from_service_account_file(file_location + "cred_Json\\creds.json", scopes=scope)
        client = gspread.authorize(creds)

        # Open the Google Spreadsheet
        spreadsheet = client.open(spreadsheet_name)

        # Select the worksheet
        worksheet = spreadsheet.worksheet(worksheet_name)

        # Clear the existing contents of the worksheet
        worksheet.clear()

        # Write the DataFrame to the worksheet starting from cell A1
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

        print("Spreadsheet successfully updated.")

    except Exception as e:
        print(f"An error occurred: {str(e)} while writing google spread")

def reading_csv():
    try:
        print("Start executing...")
        
        # Define the path to your CSV file
        csv_file_path = file_location + 'project_3_foodCartAnalysis\\hotel_booking.csv'

        # Define the name of your Google Spreadsheet
        spreadsheet_name = 'Acvin'

        # Define the name of the worksheet within the spreadsheet
        worksheet_name = 'hotel_booking'

        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Replace NaN values with an empty string ''
        df = df.fillna('')

        # Update the Google Spreadsheet
        writing_to_google_spreadsheet(df, spreadsheet_name, worksheet_name)

        print("Execution completed.")

    except Exception as e:
        print(f"An error occurred: {str(e)} while reading csv")

if __name__ == "__main__":
    reading_csv()
