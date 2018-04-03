import hyperwallet
import sys

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
paymentToken = sys.argv[4]

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

data = {
    'transition' : 'CANCELLED',
    'notes' : 'Cancel a payment upon customer request.'
}

response = api.createPaymentStatusTransition(paymentToken, data)

print response