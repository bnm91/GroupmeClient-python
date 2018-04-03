import requests

class Members:

    def __init__(self, groupmeAccessToken, groupId):
        self.groupId = groupId
        self.URL_BASE = 'https://api.groupme.com/v3'
        self.TOKEN_QUERY_STRING = '?token=' + groupmeAccessToken
    
    def add(self, **kwargs):
        '''
        Add a member the group
        Params
            members: array - objects described below. nickname is required. You must use one of the following identifiers: user_id, phone_number, or email.
                object
                    nickname (string) required
                    user_id (string)
                    phone_number (string)
                    email (string)
                    guid (string)
        '''
        load = {}
        for key, value in kwargs.items():
            if key == 'members':
                members = value
            
            load = {}
            array = []
            hasNickname = False
            hasRequiredFields = False
            for member in members:
                if 'nickname' in member:
                    hasNickname = True
                if 'user_id' in member:
                    hasRequiredFields = True
                if 'phone_number' in member:
                    hasRequiredFields = True
                if 'email' in member:
                    hasRequiredFields = True
                if hasNickname and hasRequiredFields:
                    array.append(member)
        load['members'] = array
        url = self.URL_BASE + '/groups/' + str(self.groupId) + '/members/add' + self.TOKEN_QUERY_STRING
        r = requests.post(url, json = load)
        return self.parse_response_from_json(r)

    def remove(self, membership_id):
        '''
        Remove a member from a grup
        NOTE: Creator cannot be removed
        Params
            membership_id: string — Please note that this isn't the same as the user ID. In the members key in the group JSON, this is the id value, not the user_id.
        '''
        url = self.URL_BASE + '/groups/' + str(self.groupId) + '/members/' + str(membership_id) + '/remove' + self.TOKEN_QUERY_STRING
        r = requests.post(url)
        return self.parse_response_from_json(r)
    
    def update(self, nickname):
        '''
        Update YOUR nickname in a group. The nickname must be between 1 and 50 chars
        Params
            nickname: string - YOUR new nickname
        '''
        load = {}
        load['membership'] =  {'nickname': nickname}
        url = self.URL_BASE + '/groups/' + str(self.groupId) + '/memberships/update' + self.TOKEN_QUERY_STRING
        r = requests.post(url, json = load)
        return self.parse_response_from_json(r)

    def parse_response_from_json(self, r):
        response = ''
        try:
            response = r.json()['response']
        except Exception as ex:
            response = str(ex)
        return response

