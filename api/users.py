import requests
import sys
sys.path.append('../config.py')
from config import config

URL_BASE = 'https://api.groupme.com/v3'
TOKEN_QUERY_STRING = '?token=' + config['accessToken']

class Users:
    groupId = 0

    def __init__(self):
        pass
        
    def get(self):
        ''' Get details about the authenticated user'''
        url = URL_BASE + '/users/me' + TOKEN_QUERY_STRING
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
