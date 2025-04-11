import pyautogui
import mss
from pynput import mouse
import platform
import os
from datetime import datetime


def get_pixel_color(x, y):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(monitor)
        return img.pixel(0, 0)[:3]


def play_system_sound():
    if platform.system() == "Windows":
        import winsound
        winsound.Beep(1000, 200)  # 1000 Гц, 200 мс
    elif platform.system() == "Darwin":
        os.system("afplay /System/Library/Sounds/Glass.aiff")


def save_to_file(x, y, color):
    with open("click_log.txt", "a") as f:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{now}] Координаты: ({x}, {y}), Цвет: {color}\n")


def on_click(_, __, button, pressed):
    if pressed and button.name == "left":
        x, y = pyautogui.position()  # Берём актуальные координаты курсора
        color = get_pixel_color(x, y)
        print(f"Координаты: ({x}, {y}), Цвет: {color}")
        play_system_sound()
        save_to_file(x, y, color)
    if pressed and button.name == "right":
        exit(0)


if __name__ == "__main__":
    print("Ожидание клика... Нажмите правой кнопкой мыши для выхода.")
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()
