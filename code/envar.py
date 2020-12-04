from decouple import config

def envar():
    '''
    global variables for 3rd party services
    .env file required in project root
    touch ~.env
    git ignore .env
    '''
    if DEV = 0:
        '''Google Cloud Services''''
        GOOGLE_USER = config('API_GOOGLE_USER_ENV')
        GOOGLE_KEY = config('API_GOOGLE_KEY_ENV')
        GOOGLE_DC = config('API_GOOGLE_DC_ENV')
        '''WHMCS.COM'''
        WHMCS_USER = config('API_WHMCS_USER_ENV')
        WHMCS_KEY = config('API_WHMCS_KEY_ENV')
        '''WHM'''
        WHM_USER = config('API_WHM_USER_ENV')
        WHM_KEY = config('API_WHM_KEY_ENV')
        '''Amazon Web Services'''
        AMAZON_USER = config('AMAZON_USER_ENV')
        AMAZON_KEY = config('AMAZON_KEY_ENV')

# print(envar)
