from google.oauth2 import id_token
from google.auth.transport import requests
import os

gcpKey = os.environ['GCP_KEY']

def verifyUser(token):
    if(token == 'local'): return str(0)
    elif(token == 'guest'): return str(1)
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), gcpKey)
        userId = idinfo['sub']
        return userId
    except ValueError:
        # Invalid token
        return 'invalid'