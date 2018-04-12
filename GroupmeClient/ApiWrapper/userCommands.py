from .command import Command

class GetMyUser(Command):
    ''' Get details about the authenticated user'''

    def __init__(self, groupmeAccessToken, **kwargs):
        self.args = kwargs
        super(GetMyUser, self).__init__(groupmeAccessToken, 'GET')   

    def createUrl(self):
        return self.URL_BASE + '/users/me' + self.TOKEN_QUERY_STRING
    
    def makeCall(self):
        super(GetMyUser, self).makeCall()