from ApiWrapper import groups
from ApiWrapper import members
from ApiWrapper import messages
from ApiWrapper import users





class Client(object):

    def __init__(self, groupmeAccessToken):
        self.accessToken = groupmeAccessToken
        self.groups = None
        self.Users = None
        self.messages = None
        self.members = None

    def makeCall(self, groupmeObject, call, **kwargs):
        if  groupmeObject == 'users':
            if self.Users is None:
                self.Users = users.Users(self.accessToken)
            if call == 'get':
                self.Users.get()
        
        if groupmeObject == 'groups':
            if self.groups is None:
                self.groups = groups.Groups(self.accessToken)
            getattr(self.groups, call)(**kwargs)

        if groupmeObject == 'members':
            if self.members is None:
                if kwargs.items()['groupId'] is not None:
                    self.members = members.Members(self.accessToken, kwargs.items()['groupId'])
            getattr(self.members, call)(**kwargs)
            
        if groupmeObject == 'messages':
            if self.messages is None:
                if kwargs.items()['groupId'] is not None:
                    self.messages = messages.Messages(self.accessToken, kwargs.items()['groupId'])
            getattr(self.messages, call)(**kwargs)
            














# print(messages.crosspackagetest())

# help(groups.getGroups())
# print(groups.getGroups())



# messagesInstance = messages.Messages(39628471)
# print(messagesInstance.get())
# print(messagesInstance.get())
# print(messagesInstance.unlike(152248319326115503))