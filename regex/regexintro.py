import re

# FIND PATTERNS WITHOUT REGULAR EXPRESSIONS

def isPhoneNumber(text):
    if len(text) != 12:
        return False;
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False;
    if text[3] != '-':
        return False;
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False;
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False;
    return True;

print('415-555-4242 is a phone number: ')
print(isPhoneNumber('415-555-4242'))
print('Moshi moshi is a phone number: ')
print(isPhoneNumber('Moshi moshi'))


# FIND PATTERN IN MESSAGE

message = 'Call me at 415-555-1011 tomrrow. 415-555-9999 is my office.'

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found ' + chunk)
print('Done')

# Creating Regex Objects

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Test number is 415-555-4242')
print('Phone number found: ' + mo.group())

# test: http://regexpal.com

# MORE PATTERN MATCHING!

phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex2.search('Test number is 415-555-4242')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

# multiple-assignment trick
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# \(and \) escape characters in the raw string will match actual parenthesis characters

# Check for first occurence of different options
heroRegex = re.compile(r'Batman|Tina Fey')
moH = heroRegex.search('Batman and Tina Fey')
print(moH.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
moB = batRegex.search('Batmobile lost a while')
print(moB.group())
print(moB.group(1))

# Optional group
batwomanRegex = re.compile(r'Bat(wo)?man')
mob1 = batwomanRegex.search('The adventures of Batman')
mob2 = batwomanRegex.search('The adventures of Batwoman')
print(mob1.group())
print(mob2.group())

# Matching zero or more with *, one or more with +, specific repetitions with {n} {min, max}
# by default regex are greedy (return longest string possible)
# non-greedy  version {min, max}?
batwostarRegex = re.compile(r'Bat(wo)*man')
mob3 = batwostarRegex.search('The adventures of Batwowowoman')
print(mob3.group())

# FINDALL() METHOD
phones = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(phones)

# OWN CHARACTER CLASSES
vowelRegex = re.compile(r'[aeiouAEIOU]')
vowels = vowelRegex.findall('Robocop eats baby food. BABY FOOD.')
print(vowels)

# MATCHING EVERYTHING WITH DOT-batwostarRegex
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Nacho Last Name: Herrera')
print(mo.group(1))
print(mo.group(2))
print(mo.group())

# SUBSTITUTE STRING WITH THE SUB() METHOD

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))


# REVIEW

# ? 0 or 1 of the preceding group
# * 0+ of the preceding group
# + 1+ of the preceding group
# {n} exactly n of the preceding group
# {n,} n+ ...
# {,m} 0...m
# {n,m} n...m
# {n,m}? or *? or +? nongreedy match of preceding group
# ^spam means the string must begin with spam
# spam$ means the string mujst end with spam
# . (dot) matches any char except \n
# \d \w \s digit word space
# \D \W \S anything except digit word space
# [abc] matches any character between the brackets
# [^abc] matches any char that isnt between the brackets
# CARET AND DOLAR assignment
# (.*) anything, greedy mode (.*?) for nongreedy
# re.DOTALL to match \n
# re.IGNORECASE
# re.VERBOSE to write comments
# re.compile(r'regex', re.ARG | re.ARG2 | ... )
