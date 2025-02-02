# This is an explanation of <span>alarm.py</span>
## Features ✨
- Alarm that works!!!
- Regular expression operations.
- x as a number xh = x hours, xm = x minutes xs = x seconds, can be put in any order.
## Explanation 👩‍🏫
### re module
This alarm uses Re module for the pattern:
r'(\d+)([hms])'
- r'' means it's a raw string. So it  interprets "\" as itself rather than an special symbol.
- \d+ is used for matching digits as a sequence and the '+' adds repetition.
- hms are the letter matched.
This results in a simple system to interpret numbers and characters, making it easier to set an alarm.
Rather than converting units with an external program.
### time⌚
Used time.sleep() to pause the program till the time set is finished.
- works in seconds
### datetime
used timedelta **time and datetime are different modules**
timedelta is used to get the seconds output correctly.
- Trying to use normal multiplication, resulted in an huge number without an aparent reason 
## Alarm sounds
- No alarm sounds for compatibility reasons.
In case of adding a sound playsound module is recommended. Although it will need to be install from pip.
## Docs 🕮
re -> https://docs.python.org/3/library/re.html#regular-expression-objects 
time -> https://docs.python.org/3/library/time.html 
datetime -> https://docs.python.org/3/library/datetime.html 
playsound -> https://github.com/TaylorSMarks/playsound 