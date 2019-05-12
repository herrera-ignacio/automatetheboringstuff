#! python
# mapIt.py - Launches a map in the browser with adress from clipboard or terminal

import webbroswer, sys, pyperclip
if len(sys.argv) > 1:
    # get address from terminal
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbroser.open('https://www.google.com/maps/place/' + address)
