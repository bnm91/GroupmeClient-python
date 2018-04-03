import requests

class Users:

    def __init__(self, groupmeAccessToken):
        self.accessToken = groupmeAccessToken
        self.URL_BASE = 'https://api.groupme.com/v3'
        self.TOKEN_QUERY_STRING = '?token=' + groupmeAccessToken
        
    def get(self):
        ''' Get details about the authenticated user'''
        url = self.URL_BASE + '/users/me' + self.TOKEN_QUERY_STRING
        print(url)
        return create_response(url)

def create_response(url):
    r = requests.get(url)
    return parse_response_from_json(r)

def parse_response_from_json(r):
    response = ''
    try:
        response = r.json()['response']
    except Exception as ex:
        response = str(ex)
    return response
