#! python
# multiclipboard.pyw - Saves and loads pieces of text to the multiclipboard
# Usage: python multiclipboard.pyw save <keyword> {saves clipboard to keyword}
#        python multiclipboard.pyw <keyword> {loads keyword content}
#        python multiclipboard.pyw list {loads all keywords to clipboard}

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':

    mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:

    if sys.argv[1].lower() == 'list':
        keyList = list(mcbShelf.keys())
        pyperclip.copy(str(keyList))
        print(keyList)
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()
