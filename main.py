from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import csv

exampleFile = open('outputNewCalendarEvents.csv')
exampleReader = csv.reader(exampleFile)
totalRows = 0

for row in exampleReader:
    
    print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
    totalRows = totalRows + 1

print('total rows = ' + str(totalRows))

exampleFile = open('outputNewCalendarEvents.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

loopLen = 0

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():

    # Call the Calendar API
    from datetime import datetime, timedelta
    import datefinder
    
    print('making events')
    # summary = ID-CustomerName
    # description = Item + Hookin, Out + Status
    # start_time_str =  Due At + (CURRENTDAY - DAYSOVER)
    

while loopLen < totalRows:

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

    service = build('calendar', 'v3', credentials=creds)
    
    smmry = str(exampleData[loopLen][0])
    print('Event Name: ' + smmry)

    dscrptn = str(exampleData[loopLen][1])
    print('Description: ' + dscrptn)

    #start_time = str(exampleData[loopLen][2])

    # Call the Calendar API
    from datetime import datetime, timedelta
    import datefinder

    def create_event(start_time_str, summary, duration, description, location):
        matches = list(datefinder.find_dates(start_time_str))
        if len(matches):
            start_time = matches[0]
            end_time = start_time + timedelta(hours=duration)
    
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'Canada/Pacific',
            },
            'end': {
                'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': 'Canada/Pacific',
            },
        }
        return service.events().insert(calendarId='primary', body=event).execute()

    create_event(exampleData[loopLen][2], smmry, 2, dscrptn, "bscService")
    loopLen = loopLen + 1
    

if __name__ == '__main__':
    main()
