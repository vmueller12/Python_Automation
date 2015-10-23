# Tutorial on Finadall matches in a string text
# The search Method would only find or return one value
# the findall method will look for all patterns and return a list with
# the corresponding patterns
import re
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

text = """
Here is the example text ..  number 345-234-1234 and we also have another number
which is 784-297-3333
"""

list_numbers = phoneRegex.findall(text)

print(list_numbers)

print('----------------------------------------------')

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

numbers = phoneRegex.findall(text)

print(numbers)

# return a list of tuples and each tuple contains two values for the area
# code and for the number

print('-----------------------------------------------')

# If there is no match with the pattern, it will return an empty list

phoneRegex = re.compile(r'(\d\d\d\d)-(\d\d\d\d-\d\d\d\d\d)')

numbers = phoneRegex.findall(text)

print(numbers)

"""
Shorthand character class
Represents
\d
Any numeric digit from 0 to 9.
\D
Any character that is not a numeric digit from 0 to 9.
\w
Any letter, numeric digit, or the underscore character.
(Think of this as matching “word” characters.)
\W
Any character that is not a letter, numeric digit, or the underscore character.
\s
Any space, tab, or newline character. (Think of this as matching “space” characters.)
\S
Any character that is not a space, tab, or newline.
"""

print('------------------------------------------------')


lytics = """
12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing,
8 maids a milking, 7 swans a swimming
"""

xmasRegex = re.compile(r'\d+\s\w+')
lis = xmasRegex.findall(lytics)
print(lis)

print('----------------------------------------------------')

vowelRegex = re.compile(r'[aeiouAEIOU]') # r'(a|e|i|o|u|A|E|I|O|U)'

print(vowelRegex.findall('Robocop eats baby food.'))

# Now we want to find 2 vocals in the

doubleVowel = re.compile(r'[aeiouAEIOU]{2,7}')

print(doubleVowel.findall('Robocop eats baby fooeid'))


# creating the reverse or opposite of our pattern class

consonantRegex = re.compile(r'[^aeiouAEIOU]')

print(consonantRegex.findall('Robocop eats baby food'))


