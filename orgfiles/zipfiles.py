import zipfile, os

os.chdir('C:\\') # move to folder with example.zip

# OPEN
exampleZip = zipfile.ZipFile('example.zip')


# Readinging ZIP files

exampleZip.namelist() # get contents

spamInfo = exampleZip.getinfo('spam.txt') # get file info
spamInfo.file_size
spamInfo.compress_size

print('Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo.compress_size(), 2)))

# Extracting from ZIP Files
exampleZip.extractall()
exampleZip.extract('spam.txt') # Optional path as 2nd arg

# CLOSE
exampleZip.close()

# Creating and Adding to ZIP Files

newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
