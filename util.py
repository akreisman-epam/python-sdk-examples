import os.path

def toJson( array ):
    return '{ "data" : ' + str(array) + ',\
             "count" : ' + str(len(array)) + '}'


localDir = os.path.abspath(os.path.dirname(__file__))
CLIENT_PRIVATE_KEYSET_PATH = '/app/layer7/private-jwkset'
HYPERWALLET_KEYSET_PATH = 'https://uat-api.paylution.com/jwkset'
SERVER = 'https://api.sandbox.hyperwallet.com'
