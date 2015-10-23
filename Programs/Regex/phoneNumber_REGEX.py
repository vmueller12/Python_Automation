import re

message = "Call me 415-555-1011 tomorrow, or at 415-555-9999 on my office number"

# Creating Regular Expression Object
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')


match_object = phoneNumRegex.search(message)
print(phoneNumRegex.findall(message))

area = match_object.group(1)
number = match_object.group(2)

print(area)
print(number)


batRegex = re.compile (r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobeile lost a wheel')
if mo == None:
    print("No such word pattern")
#print(mo.group(2))
