from pynput.keyboard import Key, Controller
import time

x = 0
keyboard = Controller()
def split(words):
    return[char for char in words]

while x < 10:
    time.sleep(3)
    for i in split("anything"):
        keyboard.type(i)
        time.sleep(0.1)
    x+=1
