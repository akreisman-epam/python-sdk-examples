import hyperwallet
import sys

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
userToken = sys.argv[4]
userEmail = sys.argv[5]

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

data = {
    'type': 'PAYPAL_ACCOUNT',
    'transferMethodCountry': 'US',
    'transferMethodCurrency': 'USD',
    'email': userEmail
}

response = api.createPayPalAccount(userToken, data)

print response