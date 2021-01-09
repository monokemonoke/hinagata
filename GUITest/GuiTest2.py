import pyautogui
import time
import sys

elaser = " "*80

while True:
    curmus_x,curmus_y = pyautogui.position()
    sys.stdout.write('\r'+ elaser)
    sys.stdout.write('\r'+"現在のマウス位置 [" + str(curmus_x) + "]/[" + str(curmus_y) + "]")
    sys.stdout.flush()
    time.sleep(0.05)