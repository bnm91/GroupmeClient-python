import unittest
from GroupmeClient import ApiWrapper
from GroupmeClient import client

class GetAllGroupsTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.command = ApiWrapper.groupCommands.GetAllGroups(self.fakeAccessToken)
        self.client_instance = client.Client(self.fakeAccessToken)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups?token=" + self.fakeAccessToken + '&page=1&per_page=10', 'Group command GetAllGroups: url not correct')


class FormerTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.command = ApiWrapper.groupCommands.Former(self.fakeAccessToken)
        self.client_instance = client.Client(self.fakeAccessToken)
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, "https://api.groupme.com/v3/groups/former?token=" + self.fakeAccessToken, 'Group command Former: url not correct')


class GetSingleGroupTestCase(unittest.TestCase):

    def setUp(self):
        self.fakeAccessToken = 'N09hfsiafhsdfhaskldfhj2fjf'
        self.fakeGroupId = '123452412'
        kwargs = {'id':self.fakeGroupId}
        self.command = ApiWrapper.groupCommands.GetSingleGroup(self.fakeAccessToken, **kwargs)
        
    
    def test_CreateUrl(self):
        url = self.command.createUrl()
        self.assertEqual(url, 'https://api.groupme.com/v3/groups/' + self.fakeGroupId + '?token=' + self.fakeAccessToken, 'GroupUser command GetSingleGroup: url not correct')