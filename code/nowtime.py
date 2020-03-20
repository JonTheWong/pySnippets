import time
from datetime import datetime
import pytz


# Documentation
# https://docs.python.org/3.7/library/time.html
# Based on
# https://nrc.canada.ca/en/web-clock/ 24 hr format
# Use tztime instead? https://docs.python.org/3.7/library/time.html#time.tzset as to minimize dependency

def nowtime(format):
    '''
    Show the current time based on format of systemtime.
    Hour:Minutes:Seconds = %H:M:%S colons are used for spacing
    https://docs.python.org/3.7/library/time.html#time.strftime
    Call function: ```nowtime('%H:%M:%S')```
    '''
    systime = time.localtime()
    return time.strftime(format, systime)


# print(nowtime('%H:%M:%S'))  # expected output = 01:36:44


def nowtimezone(format, timezone):
    '''
    Show the current time based on format & timezone
    Hour:Minutes:Seconds = %H:M:%S colons are used for spacing
    https://docs.python.org/3.7/library/time.html#time.strftime
    Call function: ```nowtimezone('%H:%M:%S', 'Asia/Hong_Kong')```
    Use http://pytz.sourceforge.net/#country-information to find the ideal format.
    Search https://www.iso.org/obp/ui/#search/code/ and use the Alpha-2 code for the country in question. Lowercase.
    '''
    datezone = datetime.now(pytz.timezone(timezone))
    return datezone.strftime(format)


# print(nowtimezone('%H:%M:%S', 'Asia/Hong_Kong'), ' '.join(pytz.country_timezones['hk']))  # expected output = 13:36:44 Asia/Hong_Kong
