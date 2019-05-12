# python
# stopwatch.py - A simple stopwatch program

import time

# Display instructions
print('Press ENTER to begin. Afterwards press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')

input() # Press ENTER to begin
print('Started')
startTime = time.time() # First lap start time
lastTime = startTime
lapNum = 1

# Start tracking lap times
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # Set last lap time
except KeyboardInterrupt:
    # Handle the Ctrl-C exception
    print('\nDone.')
