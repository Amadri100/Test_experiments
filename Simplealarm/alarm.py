from time import sleep
from re import findall as re_findall
from datetime import timedelta

def patternre(timme):
    "This function will interpret the strings as hours, minutes and seconds"
    pt = r'(\d+)([hms])'
    
    hour = 0
    minute = 0
    second = 0
    
    find = re_findall(pt, timme)
    
    for val, unit in find:
        if unit == 'h':
            hour = val
        elif unit == 'm':
            minute = val
        elif unit == 's':
            second = val    
    t_Delta = timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))

    print(f"Total time is {hour}:{minute}:{second} ")
    return t_Delta.total_seconds()

def start():
    print('This program is an alarm.\nTo use it write a number after the letter h,m or s\n h stands for hour, m for minute and s for second')
    tm = input(": ")
    funz = patternre(tm)
    sleep(int(funz))
    print('timer ended!')
start()