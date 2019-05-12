import pyautogui, time
input() # -> Press enter to start
time.sleep(2)
pyautogui.click()
distance = 1000
while distance > 0:
    pyautogui.dragRel(distance, 0, duration =0.05) #move right
    distance = distance -5
    pyautogui.dragRel(0, distance, duration=0.05) # move down
    pyautogui.dragRel(-distance, 0, duration=0.05) # move left
    distance = distance-5
    pyautogui.dragRel(0, -distance, duration = 0.05) # move up
