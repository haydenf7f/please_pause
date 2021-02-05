import pyautogui
import keyboard
import mouse
import time
import os


def main():
    width, height = pyautogui.size()
    x_pos = int(width / 2.56)
    y_pos = int(height / 2.4)

    print("\nThis program clicks on the video player for websites that do not have a play/pause hotkey")

    print(f'\nYour screen resolution is set to: {width} x {height}')
    print(f'Your initial click coordinates will be set to: ({x_pos}, {y_pos})')

    print("\nk = play/pause (clicks where you designate to click)")
    print("ctrl + left_mouse = sets a new coordinate to click")
    print("i + left_mouse = sets a new coordinate to click")
    print("\ = exits the program\n")

    while True:
        try:
            if keyboard.is_pressed('k'):
                pyautogui.click(x=x_pos, y=y_pos)
                continue
            if (keyboard.is_pressed('ctrl') or keyboard.is_pressed('i')) and mouse.is_pressed(button='left'):
                x_pos, y_pos = pyautogui.position()
                print(f'Position updated to: ({x_pos}, {y_pos})')
                time.sleep(1)
                continue
            if keyboard.is_pressed('\\'):
                os._exit(1)

        except:
            break


main()
