import hyperwallet
import sys

username = sys.argv[1]
password = sys.argv[2]
programToken = sys.argv[3]
userToken = sys.argv[4]
statusTransitionToken = sys.argv[5]

api = hyperwallet.Api(
    sys.argv[1],
    sys.argv[2],
    sys.argv[3]
)

response = api.getUserStatusTransition(userToken, statusTransitionToken)
print response