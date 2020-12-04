from decouple import config


# Documentation
# https://pypi.org/project/python-decouple/

def envar(ZENV):
    '''
    global variables for 3rd party services
    .env file required in project root
    '''
    global GOOGLE_CLOUD_MAPS_KEY
    if ZENV == 0:
        GOOGLE_CLOUD_MAPS_KEY = config('GOOGLE_CLOUD_MAPS_KEY')
    else:
        GOOGLE_CLOUD_MAPS_KEY = config('GOOGLE_CLOUD_MAPS_KEY_DEV')
    return


# def testvar():
#     envar(0)
#     return print(GOOGLE_CLOUD_MAPS_KEY)
#
#
# testvar()
