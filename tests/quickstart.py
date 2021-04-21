from googleapiclient.discovery import build
from google.oauth2 import service_account


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = ''


def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range="stocks!A1:B11").execute()
    values = result.get('values', [])
    print(values)


    aoa = [
        ["1/1/2020", 4000],
        ["3/3/2020", 200],
        ["1/2/2020", 100]]

    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range='stocks2!B2', valueInputOption="USER_ENTERED",
                                    body={"values": aoa})
    response = request.execute()

if __name__ == '__main__':
    main()
