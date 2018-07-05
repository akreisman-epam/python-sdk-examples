import hyperwallet
import datetime
import sys

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
sourceToken = sys.argv[4]
destinationToken = sys.argv[5]
clientTransferId = datetime.datetime.now().isoformat()

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

data = {
    'sourceToken' : sourceToken,
    'destinationToken' : destinationToken,
    'clientTransferId' : clientTransferId
}

response = api.createTransfer(data)

print response