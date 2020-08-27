# open-my-class

Just a program that opens the class page of the class that's going on / about to start.

### Format of text file

```
MINUTES_BEFORE 15
OVERLAP 0

M   9:00 10:00 www.youtube.com
M  10:35 11:05 www.github.com *
```

Settings should be at the top. The schedule is placed below, following a double line break. The format should be day of week (Su M T W R F Sa), start time, end time, URL, and an optional asterisk, each separated by one or more spaces. If the asterisk is there, then that class takes priority when there are two overlapping classes.

The user is responsible for correct input (three class times overlapping may cause the middle class to be ignored).

The following table shows the settings:

| Setting | Description | Default |
| ------------- | ------------- | ------------- |
| MINUTES_BEFORE | Number of minutes before the class to consider it "during class". | 15 |
| OVERLAP | In the case of overlapping classes. A value of 0 makes the first class take priority. A value of 1 makes the second class take priority. | 1 |
| DAYS_OF_WEEK | The abbreviations for days of the week beginning with Sunday, separated by hyphens. | Su-M-T-W-R-F-Sa |
