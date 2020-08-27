import webbrowser

MINUTES_BEFORE = 15
OVERLAP = 1
DAYS_OF_WEEK = ('M', 'T', 'W', 'H', 'F', 'Sa', 'Su')

with open('sample', 'r') as f:
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
        # Schedule
        elif len(param) == 4:
            pass

print(MINUTES_BEFORE, OVERLAP, DAYS_OF_WEEK)

webbrowser.open('http://docs.python.org/lib/module-webbrowser.html')
