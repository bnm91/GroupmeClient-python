# GroupmeClient-python
A python library that is a client for Groupme.  Not officially affiliated with Groupme

## Usage
Every command can be accessed by the library's simple client or by executing the command directly.
Simple client commands work by instantiating the Client class and passing the GroupMe object and command name to Client.makeCall
example:
```
client_instance = GroupmeClient.Client(accessToken)
client_instance.makeCall('groups', 'Update', **kwargs)
```

## Groups
Commands related to Groups GroupMe objects

### GetAllGroups
Gets all groups associated with your user
```
client_instance.makeCall('groups', 'GetAllGroups')
```

```
GroupmeClient.ApiWrapper.groupCommands.GetAllGroups(accessToken).makeCall()
```

### Former
Gets groups your user was formerly a member of
```
client_instance.makeCall('groups', 'Former')
```

```
GroupmeClient.ApiWrapper.groupCommands.Former(accessToken).makeCall()
```

### GetSingleGroup
Gets a single specified group
```
client_instance.makeCall('groups', 'GetSingleGroup')
```

```
GroupmeClient.ApiWrapper.groupCommands.GetSingleGroup(accessToken).makeCall()
```

### Create
Creates a new group
Params
name (required): string — Primary name of the group. Maximum 140 characters
description: string — A subheading for the group. Maximum 255 characters
image_url: string — GroupMe Image Service URL
share: boolean — If you pass a true value for share, we'll generate a share URL. Anybody with this URL can join the group.
```
kwargs = {'name':'Foo McBar'}
client_instance.makeCall('groups', 'Create', **kwargs)
```

```
kwargs = {'name':'Foo McBar'}
GroupmeClient.ApiWrapper.groupCommands.Create(accessToken, **kwargs).makeCall()
```

### Update
Updates a specified group
Params
id: groupid
name: string — Primary name of the group. Maximum 140 characters
description: string — A subheading for the group. Maximum 255 characters
image_url: string — GroupMe Image Service URL
share: boolean — If you pass a true value for share, we'll generate a share URL. Anybody with this URL can join the group.
```
kwargs = {'id':'1234567890', 'name':'Foo McBar', 'description': 'A GroupMe group!'}
client_instance.makeCall('groups', 'Update', **kwargs)
```

```
kwargs = {'id':'1234567890', 'name':'Foo McBar', 'description': 'A GroupMe group!'}
GroupmeClient.ApiWrapper.groupCommands.Update(accessToken, **kwargs).makeCall()
```

### Destroy
Destroys a specified group
Params
id: groupid
```
kwargs = {'id':'1234567890'}
client_instance.makeCall('groups', 'Destroy', **kwargs)
```

```
kwargs = {'id':'1234567890'}
GroupmeClient.ApiWrapper.groupCommands.Destroy(accessToken, **kwargs).makeCall()
```
