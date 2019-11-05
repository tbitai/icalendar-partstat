#!/usr/bin/env python3

import argparse
from icalendar import Calendar, Event, vText, vDatetime
from datetime import datetime
import pytz
import re


# Parse args
parser = argparse.ArgumentParser(description='''\
This script takes an iCalendar file, and prepares an edited copy of it, suitable for 
sending back as a reply to an event invitation.

Example: icalendar_partstat.py invite.ics me@example.com ACCEPTED -o invite-reply.ics''',
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('infile', help='input iCalendar file')
parser.add_argument('-o', '--outfile', help='output iCalendar file (print to stdout by default)')
parser.add_argument('email', help='attendee email for which to set the status')
parser.add_argument('status', help='status to set',
                    choices=['NEEDS-ACTION', 'ACCEPTED', 'DECLINED', 'TENTATIVE', 'DELEGATED'])
args = parser.parse_args()

# Read
with open(args.infile) as f:
    cal = Calendar.from_ical(f.read())

# Process
cal['method'] = vText('REPLY')
for subcomp in cal.subcomponents:
    if type(subcomp) == Event:
        attendees_data = subcomp['attendee']
        attendees = attendees_data if type(attendees_data) == list else [attendees_data]
        for attendee in attendees:
            if re.match(r'MAILTO:{}$'.format(args.email), attendee.to_ical().decode('utf-8'), re.IGNORECASE):
                attendee.params['partstat'] = vText(args.status)
                subcomp['last-modified'] = vDatetime(datetime.now(tz=pytz.utc))
                subcomp['dtstamp'] = vDatetime(datetime.now(tz=pytz.utc))
                break
        break

# Write
ical = cal.to_ical()
outfile = args.outfile
if not outfile:
    print(ical.decode('utf-8'))
else:
    with open(outfile, 'wb') as f:
        f.write(ical)
