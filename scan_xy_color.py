import pyautogui
import time
import mss


# Функция для получения цвета пикселя через mss
def get_pixel_color(x, y):
    with mss.mss() as sct:
        monitor = {"top": y, "left": x, "width": 1, "height": 1}
        img = sct.grab(monitor)
        return img.pixel(0, 0)[:3]


print("Переместите курсор на окно с игрой и подождите 3 секунды...")

while True:
    time.sleep(3)

    # Получаем текущие координаты курсора
    x, y = pyautogui.position()
    print(f"Координаты курсора: ({x}, {y})")

    # Получаем цвет пикселя по этим координатам
    color = get_pixel_color(x, y)
    print(f"Цвет пикселя: {color}")
