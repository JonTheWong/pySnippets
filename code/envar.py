from decouple import config

def envar():
    '''
    global variables for 3rd party services
    .env file required in project root
    touch ~.env
    git ignore .env
    forcing global var
    '''
    if DEV = 0:
        '''Google Cloud Services''''
        global GOOGLE_USER, GOOGLE_KEY, GOOGLE_DC
        GOOGLE_USER = config('API_GOOGLE_USER_ENV')
        GOOGLE_KEY = config('API_GOOGLE_KEY_ENV')
        GOOGLE_DC = config('API_GOOGLE_DC_ENV')
        '''WHMCS.COM'''
        global WHMCS_USER, WHMCS_KEY
        WHMCS_USER = config('API_WHMCS_USER_ENV')
        WHMCS_KEY = config('API_WHMCS_KEY_ENV')
        '''WHM'''
        global WHM_USER, WHM_KEY
        WHM_USER = config('API_WHM_USER_ENV')
        WHM_KEY = config('API_WHM_KEY_ENV')
        '''Amazon Web Services'''
        global AMAZON_USER, AMAZON_KEY
        AMAZON_USER = config('AMAZON_USER_ENV')
        AMAZON_KEY = config('AMAZON_KEY_ENV')

# print(envar)
