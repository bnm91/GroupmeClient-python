from .ApiWrapper import Commands
from .config import config

getGroupsCommand = Commands.groups.GetGroups(config['accessToken'])

print(getGroupsCommand.makeCall())