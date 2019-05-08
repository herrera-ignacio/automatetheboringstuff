# python
# remove files with the input ext, prints log of deleted files.

# ALTERNATIVE: send2trash third party module

import os

ext = input('Type extension to remove from dir: ')

for filename in os.listdir():
    if filename.endswith('.' + ext):
        # os.unlink(filename)
        print(filename)
