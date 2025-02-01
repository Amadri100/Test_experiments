import time
import re

def patternre(time):
    "This function will interpret the strings as hours, minutes and seconds"
    pt = r'(\d+)([hms])'
    
    hour = 0
    minute = 0
    second = 0
    
    find = re.findall(pt, time)
    
    for val, unit in find:
        if unit == 'h':
            hour = val
        elif unit == 'm':
            minute = val
        elif unit == 's':
            second = val    
    timeInSec = hour *3600 + minute *60 + second 
    
    