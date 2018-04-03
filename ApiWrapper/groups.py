import requests
import sys
sys.path.append('../config.py')
from config import config

URL_BASE = 'https://api.groupme.com/v3'
TOKEN_QUERY_STRING = '?token=' + config['accessToken']

class Groups:

    def __init__(self):
        pass


    def getGroups(self, **kwargs):
        ''' Gets all groups
            Params 
                page: integer — Fetch a particular page of results. Defaults to 1.
                per_page: integer — Define page size. Defaults to 10.
        '''
        page =  1
        per_page = 10
        for key, value in kwargs.items():
            if key == 'page':
                page = value
            elif key == 'per_page':
                per_page = value
        url = URL_BASE + '/groups' + TOKEN_QUERY_STRING +  '&page=' + str(page) + '&per_page=' + str(per_page)
        print(url)
        return create_response(url)
    
    def getFormer(self):
        ''' Gets former groups'''
        url = URL_BASE + '/groups/former' + TOKEN_QUERY_STRING
        return create_response(url)

    def getGroup(self, id):
        ''' Gets a single group by its id'''
        url = URL_BASE + '/groups/' + str(id) + TOKEN_QUERY_STRING
        print(url)
        return create_response(url)

    def createGroup(self, **kwargs):
        ''' Creates a new group
            HTTP POST
            Params
            name *: string — Primary name of the group. Maximum 140 characters
            description: string — A subheading for the group. Maximum 255 characters
            image_url: string — GroupMe Image Service URL
            share: boolean — If you pass a true value for share, we'll generate a share URL. Anybody with this URL can join the group.'''
        hasValidParam = False
        load = {}
        for key, value in kwargs.items():
            if key == 'name':
                load['name'] = value
                hasValidParam = True
            elif key == 'description':
                load['description'] = value
            elif key == 'image_url':
                load['image_url'] = value
            elif key == 'share':
                load['share'] = value
        url = URL_BASE + '/groups' + TOKEN_QUERY_STRING
        if hasValidParam:
            requests.post(url, json = load)
        else:
            return 'No valid name parameter provided'

    def updateGroup(self, id, **kwargs):
        ''' Updates specified group
            HTTP POST
            Params
                id: groupid
                kwargs
                name: string — Primary name of the group. Maximum 140 characters
                description: string — A subheading for the group. Maximum 255 characters
                image_url: string — GroupMe Image Service URL
                share: boolean — If you pass a true value for share, we'll generate a share URL. Anybody with this URL can join the group.
            Returns POST response
        '''
        load = {}
        for key, value in kwargs.items():
            if key == 'name':
                load['name'] = value
            elif key == 'description':
                load['description'] = value
            elif key == 'image_url':
                load['image_url'] = value
            elif key == 'share':
                load['share'] = value
        url = URL_BASE + '/groups/' + str(id) + '/update' + TOKEN_QUERY_STRING
        r = requests.post(url, json = load)
        return parse_response_from_json(r)

    def destroyGroup(self, id):
        ''' Destroys specified group
            Only availabe to groups creator
            HTTP POST
            Returns POST response'''
        url = URL_BASE + '/groups/' + str(id) + '/destroy' + TOKEN_QUERY_STRING
        r = requests.post(url)
        return parse_response_from_json(r)
        
    #TODO: investigate share tokens and implement this
    def joinGroup(self, id, shareToken):
        raise NotImplementedError

    #TODO: investigate how this works and implement
    def rejoinGroup(self, id):
        raise NotImplementedError

    #TODO: investigate how this works and implement
    def changeOwners(self, **kwargs):
        '''
        Changes Owner of a group (must be group's creator)
        requests required
            array — One request is object where user_id is the new owner who must be active member of a group specified by group_id.
                object
                    group_id (string) required
                    owner_id (string) required
        HTTP POST
        '''
        raise NotImplementedError

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


