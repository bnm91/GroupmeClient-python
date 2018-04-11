from command import Command

class GetGroups(Command):

    def __init__(self, groupmeAccessToken, **kwargs):
        ''' Gets all groups
            Params 
                page: integer — Fetch a particular page of results. Defaults to 1.
                per_page: integer — Define page size. Defaults to 10.
        '''
        self.accessToken = groupmeAccessToken
        self.URL_BASE = 'https://api.groupme.com/v3'
        self.TOKEN_QUERY_STRING = '?token=' + self.accessToken
        self.args = kwargs
        super(GetGroups, self).__init__('GET')
    
    def createUrl(self):
        page =  1
        per_page = 10
        for key, value in self.args.items():
            if key == 'page':
                page = value
            elif key == 'per_page':
                per_page = value
        url = self.URL_BASE + '/groups' + self.TOKEN_QUERY_STRING +  '&page=' + str(page) + '&per_page=' + str(per_page)
        return url

    def makeCall(self):
        super(GetGroups, self).makeCall()