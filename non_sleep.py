import pyautogui
from time import sleep

n = 200

for i in range(n):
    sleep(60)
    pyautogui.press(['left'])
    print(i)
