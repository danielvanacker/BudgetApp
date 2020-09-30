from google.oauth2 import id_token
from google.auth.transport import requests

def verifyUser(token):
    if(token == 'local'): return 0
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), "534582619855-hmb2rjigtsjsaojp3g8otihpkmkc36eg.apps.googleusercontent.com")
        userId = idinfo['sub']
        return userId
    except ValueError:
        # Invalid token
        return 'invalid'