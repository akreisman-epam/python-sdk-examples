import hyperwallet
import sys

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
userToken = sys.argv[4]

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

data = {
    'type' : 'PAPER_CHECK',
    'bankAccountRelationship' : 'OWN_COMPANY',
    'profileType' : 'INDIVIDUAL',
    'transferMethodCountry' : 'US',
    'transferMethodCurrency' : 'USD'
}

response = api.createPaperCheck(userToken, data)

print response