import re

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 on my office number"

# Creating Regular Expression Object
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


match_object = phoneNumRegex.search(message)
print(phoneNumRegex.findall(message))

print(match_object.group())
