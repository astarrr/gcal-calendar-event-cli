import sys
import pickle
import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import requests
import json
from datetime import datetime, timedelta


def check_credentials():
    credentials = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'google_calendar_credentials.json',
                scopes=['https://www.googleapis.com/auth/calendar'])

            credentials = flow.run_local_server(host='localhost',
                                                port=8080,
                                                authorization_prompt_message='Please visit this URL: {url}',
                                                success_message='The auth flow is complete; you may close this window.',
                                                open_browser=True)

        with open('token.pickle', 'wb') as token:
            pickle.dump(credentials, token)

    return credentials


def create_event(credentials, query):
    service = build('calendar', 'v3', credentials=credentials)

    response = requests.get("https://spsp.pythonanywhere.com/new_event", "query={}".format(query))
    response = json.loads(response.text)

    title = response['queryResult']['parameters']['title']
    time = response['queryResult']['parameters']['time']

    if type(time) == str:
        start_time = time
        end_time = (datetime.fromisoformat(start_time) + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S%z")
    else:
        try:
            start_time = response['queryResult']['parameters']['time']['date_time']
            end_time = (datetime.fromisoformat(start_time) + timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S%z")
        except:
            pass

        try:
            start_time = response['queryResult']['parameters']['time']['startTime']
        except:
            pass

        try:
            end_time = response['queryResult']['parameters']['time']['endTime']
        except:
            pass

        try:
            start_time = response['queryResult']['parameters']['time']['startDateTime']
        except:
            pass

        try:
            end_time = response['queryResult']['parameters']['time']['endDateTime']
        except:
            pass

        try:
            date = response['queryResult']['parameters']['date']
            hour = response['queryResult']['parameters']['time']

            date = datetime.fromisoformat(date)
            tz = date.tzinfo

            # hour può contenere due ore
            if type(hour) == str:
                hour = datetime.fromisoformat(hour)

                start_time = datetime.combine(date, hour.time(), tz)
                end_time = start_time + timedelta(hours=1)
            else:
                start_time = hour['startTime']
                end_time = hour['endTime']

                start_time = datetime.fromisoformat(start_time)
                end_time = datetime.fromisoformat(end_time)

                start_time = start_time.combine(date, start_time.time(), tz)
                end_time = end_time.combine(date, end_time.time(), tz)

            start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S%z")
            end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S%z")

        except:
            pass

    event = {
        "summary": title,
        'start': {
            'dateTime': start_time
        },
        'end': {
            'dateTime': end_time
        }
    }

    created_event = service.events().insert(
        calendarId='primary',
        body=event).execute()

    print(created_event['htmlLink'])

    service.close()


if __name__ == "__main__":
    cred = check_credentials()

    query = ""
    for i in range(1, len(sys.argv)):
        query = query + sys.argv[i] + " "

    create_event(cred, query)
