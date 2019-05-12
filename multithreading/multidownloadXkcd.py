#! python
# multidownloadXkcd.py - Downloads XKCD comics using multiple threads

#! python
# downloadXkcd.py - Downloads every single XKCD comic

import requests, os, bs4, threading

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

def downloadXkcd(startComic, endComic):
    for urlNumber in range(startcomic, endComic):
        # Download page
        print('Reading page http://xkcd.com/%s...' % urlNumber)
        res = requests.get('http://xkcd.com/%' + urlNumber)
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text)

        # Find URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Downloads
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

        # Save image to ./XKCD
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()


# Create and start thread objects
downloadThreads = []
for i in range(0, 1400, 100): # loops 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i+99)) # 100 arguments for iteration
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()

print('Finished execution.')
