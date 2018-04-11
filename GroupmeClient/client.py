from .ApiWrapper import groups
from .ApiWrapper import members
from .ApiWrapper import messages
from .ApiWrapper import users
# from config import config





class Client(object):

    def __init__(self, groupmeAccessToken):
        self.accessToken = groupmeAccessToken
        self.groups = None
        self.Users = None
        self.messages = None
        self.members = None

    def makeCall(self, groupmeObject, call, **kwargs):
        '''
        Currently implemented calls, by groupmeObject\n
        \n
        users
            get
        groups
            getGroups
            getFormer
            getGroup
            createGroup
            updateGroup
            destroyGroup
        members
            add
            remove
            update
        messages
            get
            create
            like

        '''

        if  groupmeObject == 'users':
            if self.Users is None:
                self.Users = users.Users(self.accessToken)
            if call == 'get':
                return self.Users.get()
        
        if groupmeObject == 'groups':
            if self.groups is None:
                self.groups = groups.Groups(self.accessToken)
            return getattr(self.groups, call)(**kwargs)

        if groupmeObject == 'members':
            if self.members is None:
                if kwargs.items()['groupId'] is not None:
                    self.members = members.Members(self.accessToken, kwargs.items()['groupId'])
            return getattr(self.members, call)(**kwargs)
            
        if groupmeObject == 'messages':
            if self.messages is None:
                if kwargs.items()['groupId'] is not None:
                    self.messages = messages.Messages(self.accessToken, kwargs.items()['groupId'])
            return getattr(self.messages, call)(**kwargs)
        
        return 'error'
            










# # # help(groups.getGroups())
# client = Client(config['accessToken'])
# print(client.makeCall('groups', 'createGroup', name='Client Test Group2'))

