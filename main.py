import os
from dotenv import load_dotenv
import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()

def connect_to_google_sheets(spreadsheet_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    json_keyfile_path = os.getenv('GOOGLE_SHEETS_CREDENTIALS')
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)
    client = gspread.authorize(credentials)

    spreadsheet = client.open(spreadsheet_name)
    
    return spreadsheet

if __name__ == "__main__":
    spreadsheet_name = 'data_science_phrases'
    spreadsheet = connect_to_google_sheets(spreadsheet_name)
    print("Connexion réussie au Google Sheet:", spreadsheet.title)
