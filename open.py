import datetime
import webbrowser

MINUTES_BEFORE = 15
OVERLAP = 1
DAYS_OF_WEEK = ('M', 'T', 'W', 'H', 'F', 'Sa', 'Su')

dayOfWeek = DAYS_OF_WEEK[datetime.date.today().weekday()]
time = datetime.datetime.now().hour * 60 + datetime.datetime.now().minute # Store time in minutes since midnight

with open('sample', 'r') as f:
    foundOne = False
    links = []
    lines = f.readlines()
    for line in lines:
        param = line.strip().split()
        # Settings
        if len(param) == 2:
            if param[0] == 'MINUTES_BEFORE':
                MINUTES_BEFORE = int(param[1])
            elif param[0] == 'OVERLAP':
                OVERLAP = int(param[1])
            elif param[0] == 'DAYS_OF_WEEK':
                x = param[1].split('-')
                if len(x) == 7:
                    DAYS_OF_WEEK = param[1].split('-')
                    today = DAYS_OF_WEEK[datetime.date.today().weekday()]
        # Schedule
        elif len(param) == 4:
            if param[0] == dayOfWeek:
                # Get start and end times
                x = param[1].split(':')
                y = param[2].split(':')
                startTime = int(x[0]) * 60 + int(x[1]) - MINUTES_BEFORE
                endTime = int(y[0]) * 60 + int(y[1])

                if startTime < time < endTime:
                    links.append(param[3])
                    if not foundOne:
                        foundOne = True
                        continue

            if foundOne == True:
                break

if len(links) == 1:
    webbrowser.open(links[0])
elif len(links) == 2:
    webbrowser.open(links[OVERLAP])

# webbrowser.open('http://docs.python.org/lib/module-webbrowser.html')
