import pyautogui
import keyboard
import mouse
import time


def start():
    x_pos = 1000
    y_pos = 600
    while True:
        try:
            if keyboard.is_pressed('k'):
                pyautogui.click(x=x_pos, y=y_pos)
                continue
            if keyboard.is_pressed('ctrl') and mouse.is_pressed(button='left'):
                x_pos, y_pos = pyautogui.position()
                print(f'Position updated to: ({x_pos}, {y_pos})')
                time.sleep(1)
                continue
            if keyboard.is_pressed('\\'):
                exit()

        except:
            break


start()

