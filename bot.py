import pyautogui, time
time.sleep(10)
f = open("msgs.txt","r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
