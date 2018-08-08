import hyperwallet
import sys
import util

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
userToken = sys.argv[4]
prepaidCardToken = sys.argv[5]
encryptionEnabled = sys.argv[6]

hyperwalletEncryption = None;
if encryptionEnabled == 'true':
    hyperwalletEncryption = {
        'clientPrivateKeySetLocation' : util.CLIENT_PRIVATE_KEYSET_PATH,
        'hyperwalletKeySetLocation' : util.HYPERWALLET_KEYSET_PATH
    }

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3],
    util.SERVER,
    hyperwalletEncryption
)

data = {
    'token' : prepaidCardToken,
    'userToken' : userToken,
    'cardPackage': 'DEFAULT',
    'cardNumber' : '4149629391723970'
}

response = api.updatePrepaidCard(userToken, prepaidCardToken, data)

print response