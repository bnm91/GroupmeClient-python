from api import groups
from api import members
from api import messages

# print(messages.crosspackagetest())

# help(groups.getGroups())
# print(groups.getGroups())



messagesInstance = messages.Messages(39628471)
# print(messagesInstance.get())
print(messagesInstance.get())
print(messagesInstance.unlike(152248319326115503))