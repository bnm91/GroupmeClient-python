from .command import Command

class GetGroups(Command):
    ''' Gets all groups
        Params 
            page: integer — Fetch a particular page of results. Defaults to 1.
            per_page: integer — Define page size. Defaults to 10.
    '''

    def __init__(self, groupmeAccessToken, **kwargs):
        self.args = kwargs
        super(GetGroups, self).__init__(groupmeAccessToken, 'GET')
    
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


class GetFormer(Command):
    ''' Gets former groups'''

    def __init__(self, groupmeAccessToken, **kwargs):
        self.args = kwargs
        super(GetFormer, self).__init__(groupmeAccessToken, 'GET')

    def createUrl(self):
        return self.URL_BASE + '/groups/former' + self.TOKEN_QUERY_STRING
    
    def makeCall(self):
        super(GetFormer, self).makeCall()


class GetGroup(Command):
    ''' Gets a single group by its id'''

    def __init__(self, groupmeAccessToken, **kwargs):
        self.args = kwargs
        super(GetGroup, self).__init__(groupmeAccessToken, 'GET')
    
    def createUrl(self):
        id = 0
        for key, value in self.args.items():
            if key == 'id':
                id = value
        url = self.URL_BASE + '/groups/' + str(id) + self.TOKEN_QUERY_STRING
        return url
    
    def makeCall(self):
        super(GetGroup, self).makeCall()
    
class CreateGroup(Command):
    ''' Creates a new group
        HTTP POST
        Params
        name *: string — Primary name of the group. Maximum 140 characters
        description: string — A subheading for the group. Maximum 255 characters
        image_url: string — GroupMe Image Service URL
        share: boolean — If you pass a true value for share, we'll generate a share URL. Anybody with this URL can join the group.'''
    
    def __init__(self, groupmeAccessToken, **kwargs):
        self.args = kwargs
        super(CreateGroup, self).__init__(groupmeAccessToken, 'POST')

    def createUrl(self):
        return self.URL_BASE + '/groups' + self.TOKEN_QUERY_STRING

    def createLoad(self):
        hasValidParam = False
        load = {}
        for key, value in self.args.items():
            if key == 'name':
                load['name'] = value
                hasValidParam = True
            elif key == 'description':
                load['description'] = value
            elif key == 'image_url':
                load['image_url'] = value
            elif key == 'share':
                load['share'] = value
        if hasValidParam:
            return load
        else:
            return 'No valid name parameter provided'
        
    def makeCall(self):
        super(CreateGroup, self).makeCall()

class UpdateGroup(Command):
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

    def __init__(self, groupmeAccessToken, **kwargs):
        self.args = kwargs
        super(UpdateGroup, self).__init__(groupmeAccessToken, 'POST')

    def createUrl(self):
        id = 0
        for key, value in self.args.items():
            if key == 'id':
                id = value
        return self.URL_BASE + '/groups/' + str(id) + '/update' + self.TOKEN_QUERY_STRING

    def createLoad(self):
        load = {}
        for key, value in self.args.items():
            if key == 'name':
                load['name'] = value
            elif key == 'description':
                load['description'] = value
            elif key == 'image_url':
                load['image_url'] = value
            elif key == 'share':
                load['share'] = value
        return load

    def makeCall(self):
        super(UpdateGroup, self).makeCall()


class DestroyGroup(Command):
    ''' Destroys specified group
        Only availabe to groups creator
        HTTP POST
        Returns POST response'''
    
    def __init__(self, groupmeAccessToken, **kwargs):
        self.args = kwargs
        super(DestroyGroup, self).__init__(groupmeAccessToken, 'POST')

    def createUrl(self):
        id = 0
        for key, value in self.args.items():
            if key  == 'id':
                id = value
        url = self.URL_BASE + '/groups/' + str(id) + '/destroy' + self.TOKEN_QUERY_STRING
        return url

    def makeCall(self):
        super(DestroyGroup, self).makeCall()


#TODO: investigate share tokens and implement this
class JoinGroup(Command):

    def __init__(self, groupmeAccessToken, **kwargs):
        raise NotImplementedError


#TODO: investigate how this works and implement
class RejoinGroup(Command):

    def __init__(self, groupmeAccessToken, **kwargs):
        raise NotImplementedError


class ChangeOwner(Command):
    '''
    Changes Owner of a group (must be group's creator)
    requests required
        array — One request is object where user_id is the new owner who must be active member of a group specified by group_id.
            object
                group_id (string) required
                owner_id (string) required
    HTTP POST
    '''

    def __init__(self, groupmeAccessToken, **kwargs):
        raise NotImplementedError