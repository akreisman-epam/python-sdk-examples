import hyperwallet
import datetime
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import util

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
sourceToken = sys.argv[4]
destinationToken = sys.argv[5]
encryptionEnabled = sys.argv[6]
clientTransferId = datetime.datetime.now().isoformat()

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
    'sourceToken' : sourceToken,
    'destinationToken' : destinationToken,
    'clientTransferId' : clientTransferId
}

response = api.createTransfer(data)

print response