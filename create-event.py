event = {
  'summary': 'Appointment',
  'location': 'Somewhere',
  'start': {
    'dateTime': '2011-06-03T10:00:00.000-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'end': {
    'dateTime': '2011-06-03T10:25:00.000-07:00',
    'timeZone': 'America/Los_Angeles'
  },
  'recurrence': [
    'RRULE:FREQ=WEEKLY;UNTIL=20110701T170000Z',
  ],
  'attendees': [
    {
      'email': 'attendeeEmail',
      # Other attendee's data...
    },
    # ...
  ],
}

recurring_event = service.events().insert(calendarId='primary', body=event).execute()

print (recurring_event['id'])