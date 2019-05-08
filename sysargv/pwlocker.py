#! python 3
# pwlocker.py - An insecure password locker program

PASSWORDS = {'ignacioromanherrera@gmail.com' : 'testpw',
             'testaccount': '1234',
             'NASA': 'rocketman'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pwlocker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
