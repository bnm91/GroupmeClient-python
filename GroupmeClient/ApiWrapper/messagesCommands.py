from .command import Command

class GetMessages(Command):
    '''
    Retrieve messages for a group.
    By default, messages are returned in groups of 20, ordered by created_at descending. This can be raised or lowered by passing a limit parameter, up to a maximum of 100 messages.
    Params
        before_id:  string — Returns messages created before the given message ID
        since_id:   string — Returns most recent messages created after the given message ID
        after_id:   string — Returns messages created immediately after the given message ID
        limit:      integer — Number of messages returned. Default is 20. Max is 100.
    '''

    def __init__(self, groupmeAccessToken, groupId, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        super(GetMessages, self).__init__(groupmeAccessToken, 'GET')   

    def createUrl(self):
        query_string = ''
        for key, value in self.args.items():
            if key == 'before_id':
                query_string += '&before_id='
                query_string += str(value)
            elif key == 'since_id':
                query_string += '&since_id='
                query_string += str(value)
            elif key == 'after_id':
                query_string += '&after_id='
                query_string += str(value)
            elif key == 'limit':
                query_string += '&limit='
                query_string += str(value)
        
        return self.URL_BASE + '/groups/' + str(self.groupId) + '/messages' + self.TOKEN_QUERY_STRING + query_string

    def makeCall(self):
        super(GetMessages, self).makeCall()


class CreateMessage(Command):
    '''
    Send a message to a group
    If you want to attach an image, you must first process it through groupme image service
    HTTP POST
    Params
        source_guid (required): string — Client-side IDs for messages. This can be used by clients to set their own identifiers on messages, but the server also scans these for de-duplication. That is, if two messages are sent with the same source_guid within one minute of each other, the second message will fail with a 409 Conflict response. So it's important to set this to a unique value for each message.
        text (required):        string — This can be omitted if at least one attachment is present. The maximum length is 1,000 characters.
        attachments:            array — A polymorphic list of attachments (locations, images, etc). You may have You may have more than one of any type of attachment, provided clients can display it.
            *elements must be one of the following object types*
            object
                type (string) — “image” required
                url (string) required — Must be an image service (i.groupme.com) URL
            object
                type (string) — “location” required
                name (string) required
                lat (string) required
                lng (string) required
            object
                type (string) — “split” required
                token (string) required
            object
                type (string) — “emoji” required
                placeholder (string) — “☃” required
                charmap (array) — “[{pack_id},{offset}]” required
            object
                type (string) - "mentions" required
                user_ids (array) - array of user ids of members being tagged
    '''

    def __init__(self, groupmeAccessToken, groupId, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        super(CreateMessage, self).__init__(groupmeAccessToken, 'POST')  

    def createUrl(self):
        return self.URL_BASE + '/groups/' + str(self.groupId) + '/messages' + self.TOKEN_QUERY_STRING 
    
    def createLoad(self):
        load = {}
        message = {}
        array = []
        for key, value in self.args.items():
            if key == 'source_guid':
                message['source_guid'] = value
            elif key == 'text':
                message['text'] = value
            elif key == 'attachments':
                attachments = value
                isValidAttachment = False

                #TODO: each type is required to be a specific string, implement checks for that
                #   see groupme api documentation
                for attachment in attachments:
                    if 'type' in attachment and 'url' in attachment:
                        isValidAttachment = True
                    if 'type' in attachment and 'name'  in attachment and 'lat' in attachment and 'lng' in attachment:
                        isValidAttachment = True
                    if 'type' in attachment and 'token' in attachment:
                        isValidAttachment = True
                    if 'type' in attachment and 'placeholder' in attachment and 'charmap' in attachment:
                        isValidAttachment = True
                    if isValidAttachment:
                        array.append(attachment)
        message['attachments'] = array
        load['message'] = message
        return load

    def makeCall(self):
        super(CreateMessage, self).makeCall()


class LikeMessage(Command):
    '''Likes specified message'''

    def __init__(self, groupmeAccessToken, groupId, **kwargs):
        self.args = kwargs
        self.groupId = groupId
        super(LikeMessage, self).__init__(groupmeAccessToken, 'POST')  

    def createUrl(self):
        message_id = 0
        for key, value in self.args.items():
            if key == 'message_id':
                message_id = value
        return self.URL_BASE + '/messages/' + str(self.groupId) + '/' + str(message_id) + '/like' + self.TOKEN_QUERY_STRING

    def makeCall(self):
        super(LikeMessage, self).makeCall()