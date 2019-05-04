#! python3
# bulletPointerAdder.py - Adds Wikipedia bullet points to each line

# step 1: get text from clipboard
# step 2: add a star and space to the beggining of each line
# step 3: paste this new text to the clipboard

import pyperclip
text = pyperclip.paste()

# separte and modify lines
lines = text.split('\n')
for i in range(len(lines)):
    lines [i] = '* ' + lines[i]

# make a single string value
text = '\n'.join(lines)

pyperclip.copy(text)
