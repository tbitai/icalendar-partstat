# icalendar-partstat

iCalendar event participation status editor.

```
$ icalendar_partstat.py invite.ics me@example.com ACCEPTED -o invite-reply.ics
```

This script takes an iCalendar file, and prepares an edited copy of it, suitable for sending back as a reply to an event invitation. 

See the help for detailed usage information:

```
$ icalendar_partstat.py -h
```

## Requirements

- Python 3

- iCalendar for Python 4.0.3
  
  Install with
  
  ```
  $ pip install icalendar==4.0.3
  ```
  
  or simply using the `requirements.txt` included in the repository:
  
  ```
  $ pip install -r requirements.txt
  ```
