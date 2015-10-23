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

#? 0 or 1 time
#---------------#
print('----------------------------------------')
#batRegex = re.compile(r'Batman|Batwoman')
batRegex = re.compile(r'(Bat)(wo)?(man)?')
mo = batRegex.search('The Adventures of Batman')
print(mo.group())

# * 0 or many more times
print('-----------------------------------------')

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search("Batwowowowowowoman")
print(mo.group())

# + 1 or many more times, can not be 0
print('------------------------------------------')

batRegex = re.compile(r'Bat(wo)+man')
if batRegex.search('Batman') == None:
    print("Wo does not exsist")


print('--------------------------------------------')
# using {3} for getting the group exactly 3 times

batRegex = re.compile(r'(Ha){3}')
if batRegex.search('HaHa') == None:
    print('No match')

if batRegex.search('HaHaHa') != None:
    print('Match')

print(batRegex.search('HameHaHaHa').group())

print('----------------------------------------------')


# using {3,5} is a range of repetition 3 timies min on 5 times max
# greedy matches python will alwys look for the maximum match first
digitRegex = re.compile(r'(\d){3,5}')
print(digitRegex.search('12131311').group())
# now we will implement none greedy match with the smallest possible match
print('------------------------------------')
digitRegex = re.compile(r'(\d){3,5}?')
print(digitRegex.search('1232312312').group())
