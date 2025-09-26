import pyautogui
from time import sleep

#n = int(input('PCスリープさせたくない時間(min)を入力してください ※半角数字>>>'))

n = 200


for i in range(n):
    sleep(60)
    pyautogui.press(['left'])
    print(i)


n = 64
n    = 64

