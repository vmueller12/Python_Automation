#! python 3

import re, pyperclip

# TODO: Create a regex for phone numbers

re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-000, 555-0000 ext 12345, ext. 12345, x12345

((\d\d\d)|(\(\d\d\d)))?    # area code (optinal)    
(\s|-)                     # first separator
\d\d\d                     # first 3 digits
-                          # separator
\d\d\d\d                   # last 4 digits
((ext(\.)?\s|x)     (\d{2,5}))    # extension (optional)

''', re.VERBOSE)

# TODO: Create a regex for email addresses

# TODO: Get the text off the clipboard

# TODO: Extract the email/phone from this text

# TODO: Copy the extravted email/phone to the clipboard
