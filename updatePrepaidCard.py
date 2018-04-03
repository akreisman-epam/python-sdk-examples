import hyperwallet
import sys

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
userToken = sys.argv[4]
prepaidCardToken = sys.argv[5]

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

data = {
    'token' : prepaidCardToken,
    'userToken' : userToken,
    'cardPackage': 'DEFAULT',
    'cardNumber' : '4149629391723970'
}

response = api.updatePrepaidCard(userToken, prepaidCardToken, data)

print response