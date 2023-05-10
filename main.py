import pyautogui
from time import sleep
from random import choice

lst = ["Hello", "Hi", "I am robot", "Welcome"]

for i in range(10):
    sleep(2)
    pyautogui.click(592, 993)   # Your box message location on screen!
    pyautogui.write(choice(lst), interval=0.1)
    pyautogui.press("enter")
