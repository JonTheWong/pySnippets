import time


# Documentation
# https://docs.python.org/3.7/library/time.html
# Based on
# https://nrc.canada.ca/en/web-clock/ 24 hr format


def nowtime(format):
    '''
    Show the current time based on format
    Hour:Minutes:Seconds = %H:M:%S colons are used for spacing
    https://docs.python.org/3.7/library/time.html#time.strftime
    Call function: ```nowtime('%H:%M:%S')```
    '''
    systime = time.localtime()
    formattime = time.strftime(format, systime)
    return formattime


# print(nowtime('%H:%M:%S'))  # expected output = 01:36:44
