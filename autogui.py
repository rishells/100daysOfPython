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

# time.sleep(5)
# pg.hotkey("win","r")
# pg.typewrite("https://www.youtube.com/watch?v=t1NxNInQW9Q&ab_channel=EduardoRosas-FinanzasPersonales=45s\n")
# time.sleep(2)
# pg.typewrite("k")
# pg.hotkey("win","r")
# pg.typewrite("notepad\n")
# time.sleep(1)
# pg.typewrite("This was a triumph\n")
# pg.hotkey("ctrl")
# pg.hotkey("ctrl")
# pg.hotkey("ctrl")
# pg.hotkey("ctrl")
# pg.hotkey("ctrl")
# pg.hotkey("ctrl")
# pg.hotkey("ctrl")
# pg.hotkey("ctrl")
# pg.sleep(3)



