from .command import Command

class Add(Command):
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

    def __init__(self, groupmeAccessToken, groupId, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        super(Add, self).__init__(groupmeAccessToken, 'POST')   

    def createUrl(self):
        print(self.groupId)
        return self.URL_BASE + '/groups/' + str(self.groupId) + '/members/add' + self.TOKEN_QUERY_STRING
    
    def createLoad(self):
        load = {}
        members = []
        array = []
        for key, value in self.args.items():
            if key == 'members':
                members = value
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
        return load

    def makeCall(self):
        return super(Add, self).makeCall()


class Remove(Command):
    '''
    Remove a member from a grup
    NOTE: Creator cannot be removed
    Params
        membership_id: string — Please note that this isn't the same as the user ID. In the members key in the group JSON, this is the id value, not the user_id.
    '''

    def __init__(self, groupmeAccessToken, groupId, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        super(Remove, self).__init__(groupmeAccessToken, 'POST')   
    
    def createUrl(self):
        membership_id = 0
        for key, value in self.args.items():
            if key == 'membership_id':
                membership_id = value
        
        url = self.URL_BASE + '/groups/' + str(self.groupId) + '/members/' + str(membership_id) + '/remove' + self.TOKEN_QUERY_STRING
        return url
    
    def makeCall(self):
        return super(Remove, self).makeCall()


class Update(Command):
    '''
    Update YOUR nickname in a group. The nickname must be between 1 and 50 chars
    Params
        nickname: string - YOUR new nickname
    '''

    def __init__(self, groupmeAccessToken, groupId, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        super(Update, self).__init__(groupmeAccessToken, 'POST')   

    def createUrl(self):
        return self.URL_BASE + '/groups/' + str(self.groupId) + '/memberships/update' + self.TOKEN_QUERY_STRING

    def createLoad(self):
        nickname = ''
        for key, value in self.args.items():
            if key == 'nickname':
                nickname = value

        load = {}
        load['membership'] =  {'nickname': nickname}
        return load

    def makeCall(self):
        super(Update, self).makeCall()


