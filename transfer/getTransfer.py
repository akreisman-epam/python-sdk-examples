import hyperwallet
import sys

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
transferToken = sys.argv[4]

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

response = api.getTransfer(transferToken)

print response