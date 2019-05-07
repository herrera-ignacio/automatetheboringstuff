#! python
# phoneAndEmail.py - Finds email addresses and Argentina's phone numbers on clipboard

import pyperclip, re

# PHONE REGEX

phoneRegex = re.compile(r'''(
    (\d{3})?                        # 3 first digits or code
    (\s|-|\.)?                      # separator
    (\d{3})                         # 3 middle digits
    (\s|-|\.)                       # separator
    (\d{4}\s*)                      # 4 last digits, must end with this
    ((ext|x|ext.)\s*(\d{2,5}))?     # extension
    )''', re.VERBOSE)

# EMAIL REGEX

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+               # username
    @                               # @ symbol
    [a-zA-z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})               # dot-something
)''', re.VERBOSE)

# FIND MATCHES IN CLIPBOARD

text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
    phoneNum = "-".join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# COPY RESULTS TO CLIPBOARD

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Found matches and copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
