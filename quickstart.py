from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup
import requests
import get_docsizes

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of the spreadsheet.
READ_RANGE = 'A1:AA1000'
CLEAR = 'A3:B32'
MAIN_RANGE= 'A2:Z8'
SCRIPT_RANGE = 'A9:AA1000'

MY_SPREADSHEET_ID = '1eVV4O_HcU_BiETm3AyHIPgmXO9FMdBGGwwf6k-T31fc'

def Create_Service():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    return service

# Call the Sheets API and Fetch URL from Sheet
def Read_From_Sheet(service):
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=MY_SPREADSHEET_ID,
                                range=READ_RANGE).execute()
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        for row in values:
            rowText = ''
            for column in row:
                rowText += '%s' % column
            # print(rowText)
        url = values[0][1]
        print('Url Loaded')
        return url

# Clears Old Data
def Clear_Data(service):
    request = service.spreadsheets().values().clear(
        spreadsheetId=MY_SPREADSHEET_ID,
        range=CLEAR
    ).execute()

# Exports Main Data
def Export_Main_Data(service, docSize, headSize, bodySize, allScriptSizes):
     # Updates Spreadsheet with Doc Size
    restOfBody = bodySize - allScriptSizes
    response_date = service.spreadsheets().values().update(
        spreadsheetId=MY_SPREADSHEET_ID,
        valueInputOption='RAW',
        range=MAIN_RANGE,
        body=dict(
            majorDimension='COLUMNS',
            values=[['','Document Size:', 'Body Size:', 'Script Total Size:','Head Size:','Body Excluding Scripts:','Script Type'],
                    ['',docSize, bodySize, allScriptSizes, headSize, restOfBody,'Script Size (bytes)']])
    ).execute()

#Exports Scripts Data
def Export_Data_To_Sheets(service, scriptIds, scriptSizes):
    # Updates Spreadsheet with Doc Size 
    response_date = service.spreadsheets().values().update(
        spreadsheetId=MY_SPREADSHEET_ID,
        valueInputOption='RAW',
        range=SCRIPT_RANGE,
        body=dict(
            majorDimension='COLUMNS',
            values=[scriptIds,scriptSizes])
    ).execute()
    print('Sheet successfully Updated')


def main():
    # Set up google api
    service = Create_Service()

    # Get Url from google sheets
    url = Read_From_Sheet(service)

    # Pulls the data from iris for that URL
    docSize, headSize, bodySize, scriptSizes, scriptIds, allScriptSizes = get_docsizes.Parse_HTML(url)

    # Update Spreadsheet
    Clear_Data(service)
    Export_Main_Data(service, docSize, headSize, bodySize, allScriptSizes)
    Export_Data_To_Sheets(service, scriptIds, scriptSizes)

if __name__ == "__main__":
    main()
