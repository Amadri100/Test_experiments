import time
import re
import os

def patternre(timme):
    "This function will interpret the strings as hours, minutes and seconds"
    pt = r'(\d+)([hms])'
    
    hour = 0
    minute = 0
    second = 0
    
    find = re.findall(pt, timme)
    
    for val, unit in find:
        if unit == 'h':
            hour = val
        elif unit == 'm':
            minute = val
        elif unit == 's':
            second = val    
    timeInSec = hour *3600 + minute *60 + second 
    print(f"Total time is {hour}:{minute}:{second} ")
    return timeInSec

def start():
    print('This program is an alarm.\nTo use it write a number after the letter h,m or s\n h stands for hour, m for minute and s for second')
    tm = input(": ")
    funz = patternre(tm)
    time.sleep(int(funz))
    print('timer ended')
start()