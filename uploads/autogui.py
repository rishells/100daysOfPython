import pyautogui as pg
import time
import random



x_rand_position = random.randint(0,500)
y_rand_position = random.randint(0,500)


pg.FAILSAFE = False
while True:
    time.sleep(250)
    for i in range(0,5):
        pg.moveTo(x_rand_position, i * 5)
    for i in range(0, 1):
        pg.press('ctrl')
        #pg.hotkey('alt','tab')





